from rest_framework import serializers

from home.models import SurveyResponse, SurveyStartJob


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyStartJob
        fields = ['unit', 'start1', 'end1', 'organ1']


class SurveySerializer(serializers.ModelSerializer):
    jobs = JobsSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = ['fullname', 'company', 'registerDate', 'fieldstudy', 'Grade', 'univercity',
                  'success', 'money', 'g15', 'g1', 'g2', 'languageint',
                  'language', 'learning',
                  'foregin', 'g3', 'g4', 'sport', 'freetime', 'book', 'news', 'work', 'ngo', 'goodwork', 'outfactory',
                  'MBTI', 'route', 'reasons', 'sort', 'description', 'pointwork', 'process', 'lie', 'g10', 'goodday', 'hard',
                  'hard2', 'age', 'gender', 'knowlage', 'personality',
                  'like', 'dislike', 'creative', 'leader', 'entrepreneur', 'star',
                  'g17', 'g18', 'is_read', 'broke', 'suggest', 'area', 'newarea', 'solution', 'jobs']

    def create(self, validated_data):
        jobs_data = validated_data.pop('jobs')
        survey = SurveyResponse.objects.create(**validated_data)
        for job in jobs_data:
            SurveyStartJob.objects.create(SR=survey, **job)
        return survey.pk
