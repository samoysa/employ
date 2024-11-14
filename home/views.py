# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from collections import namedtuple
from datetime import datetime

from django import template
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.db import connections
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from home.models import SurveyResponse
from home.serializers import SurveySerializer


class SurveyWizardView(TemplateView):
    template_name = 'home/wizard2.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyWizardView, self).get_context_data()
        return context


class index(TemplateView):
    template_name = 'home/welcome.html'

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data()
        return context


class Complete(TemplateView):
    template_name = 'home/end.html'

    def get_context_data(self, **kwargs):
        context = super(Complete, self).get_context_data()
        return context


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def add_surveys(request):
    try:
        item = SurveySerializer(data=request.data)
        # if SurveyResponse.objects.filter(personalcode__exact=request.data['personalcode']).exists():
        #     error = serializers.ValidationError('شماره پرسنلی قبلا در نظرسنجی شرکت کرده است')
        #     error.status_code = status.HTTP_409_CONFLICT
        #     raise error
        if item.is_valid():
            item.save()
            return Response('save Data.', status=status.HTTP_200_OK)
        else:
            return Response({'error': item.errors}, status=status.HTTP_403_FORBIDDEN)
            # return Response(list(item.errors.items())[0], status=status.HTTP_403_FORBIDDEN)
    except serializers.ValidationError as e:
        return Response({'error': e.detail[0]}, status=e.status_code)
    except Exception as e:
        return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
