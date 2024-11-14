from import_export import resources
from .models import SurveyResponse, SurveyStartJob


class SurveyResource(resources.ModelResource):

    def dehydrate_id(self, job):
        data = []
        for i in SurveyStartJob.objects.filter(SR__exact=job.id):
            data.append('(' + i.unit + '--' + i.start1 + '--' + i.end1 + '--' + i.organ1 + ')')
        joined_string = ",".join(data)
        return str(joined_string)

    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'id':
                headers[i] = "سوابق شغلی"
            elif h == 'languageint':
                headers[i] = "زبان قومی"
            elif h == 'language':
                headers[i] = " زبان خارجی"
            elif h == 'foregin':
                headers[i] = "تحصیل در خارج"
            elif h == 'g1':
                headers[i] = "تسلط به قانون تجارت بین الملل"
            elif h == 'g2':
                headers[i] = "تسلط به دانش قراردادها"
            elif h == 'g3':
                headers[i] = "توامندی های عمومی"
            elif h == 'g4':
                headers[i] = "توامندی در ویرایش متون"
            elif h == 'sport':
                headers[i] = "وزش و هنر"
            elif h == 'book':
                headers[i] = "مطالعه کتاب"
            elif h == 'work':
                headers[i] = "دانش بنیان"
            elif h == 'goodwork':
                headers[i] = "کار خیر"
            elif h == 'outfactory':
                headers[i] = "روابط اجتماعی و حرفه ای"
            elif h == 'route':
                headers[i] = "الگو"
            elif h == 'reasons':
                headers[i] = "سه دلیل برای کار کردن"
            elif h == 'sort':
                headers[i] = "اهمیت وجوه زندگی"
            elif h == 'description':
                headers[i] = "توصیف 5 کلمه"
            elif h == 'pointwork':
                headers[i] = "سه نقطه مثبت "
            elif h == 'process':
                headers[i] = "نتیجه یا فرآیند"
            elif h == 'lie':
                headers[i] = "دروغ گفتن"
            elif h == 'g10':
                headers[i] = "جایگاه فعلی شما بر اساس نقاط قوت"
            elif h == 'goodday':
                headers[i] = "روز ایده آل"
            elif h == 'hard':
                headers[i] = "پرچالش ترین"
            elif h == 'hard2':
                headers[i] = "راهکار اثر بخش"
            elif h == 'learning':
                headers[i] = "یادگیری مهارت"
            elif h == 'success':
                headers[i] = "تعریف موفقیت"
            elif h == 'money':
                headers[i] = "دریافت سرمایه"
            elif h == 'g15':
                headers[i] = "رضایت از گذشته"
            elif h == 'like':
                headers[i] = "علاقه مندی به حرفه خود"
            elif h == 'dislike':
                headers[i] = "عدم علاقه به حرفه خود"
            elif h == 'entrepreneur':
                headers[i] = "ویژگی کارآفرین"
            elif h == 'star':
                headers[i] = "علت ستاره بودن"
            elif h == 'broke':
                headers[i] = "تجربه شکست"
            elif h == 'g17':
                headers[i] = "مواجهه با چند مساله کاری"
            elif h == 'g18':
                headers[i] = "مواجعه با مشکل پیچیده"
            elif h == 'suggest':
                headers[i] = "پیشنهاد تغییر"
            elif h == 'area':
                headers[i] = "حوزه فعالیت در آینده"
            elif h == 'newarea':
                headers[i] = "حوزه جدید"
            elif h == 'solution':
                headers[i] = "راه حل مشکل و ضعف"
        return headers

    class Meta:
        model = SurveyResponse
