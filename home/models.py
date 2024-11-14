from django.db import models


class SurveyResponse(models.Model):
    fullname = models.CharField(max_length=255, blank=False, null=False, verbose_name='نام و نام خانوادگی')
    company = models.CharField(max_length=30, blank=False, null=False, verbose_name='شرکت استخدامی')
    registerDate = models.CharField(max_length=10, blank=False, null=False, verbose_name='تاریخ استخدام')
    fieldstudy = models.CharField(max_length=255, blank=False, null=False, verbose_name='رشته تحصیلی')
    Grade = models.CharField(max_length=30, blank=False, null=False, verbose_name='مقطع تحصیلی')
    univercity = models.CharField(max_length=255, blank=False, null=False, verbose_name='دانشگاه محل تحصیل')

    languageint = models.CharField(max_length=255, blank=False, null=False, verbose_name='زبان قومی')
    language = models.CharField(max_length=255, blank=False, null=False, verbose_name='زبان خارجی')
    foregin = models.CharField(max_length=255, blank=False, null=False, verbose_name='تحصیل در خارج')
    g1 = models.SmallIntegerField(blank=False, null=False, verbose_name='تسلط به قانون تجارت بین الملل')
    g2 = models.SmallIntegerField(blank=False, null=False, verbose_name='تسلط به دانش قراردادها')
    g3 = models.SmallIntegerField(blank=False, null=False, verbose_name='توامندی های عمومی')

    g4 = models.SmallIntegerField(blank=False, null=False, verbose_name='توامندی در ویرایش متون')
    sport = models.CharField(max_length=255, blank=False, null=False, verbose_name='وزش و هنر')
    freetime = models.CharField(max_length=255, blank=False, null=False, verbose_name='اوقات فراغت')
    book = models.CharField(max_length=255, blank=False, null=False, verbose_name='مطالعه کتاب')
    news = models.CharField(max_length=255, blank=False, null=False, verbose_name='اخبار روز')
    work = models.CharField(max_length=255, blank=False, null=False, verbose_name='دانش بنیان')
    ngo = models.CharField(max_length=255, blank=False, null=False, verbose_name='NGO')
    goodwork = models.CharField(max_length=255, blank=False, null=False, verbose_name='کار خیر')
    outfactory = models.TextField(blank=False, null=False, verbose_name='روابط اجتماعی و حرفه ای')

    MBTI = models.CharField(max_length=255, blank=False, null=False, verbose_name='تست MBTI')

    route = models.TextField(blank=False, null=False, verbose_name='الگو')
    reasons = models.TextField(blank=False, null=False, verbose_name='سه دلیل برای کار کردن')
    sort = models.CharField(max_length=255, blank=False, null=False, verbose_name='اهمیت وجوه زندگی')
    description = models.TextField( blank=False, null=False, verbose_name='توصیف 5 کلمه')
    pointwork = models.TextField( blank=False, null=False, verbose_name='سه نقطه مثبت و منفی')
    process = models.TextField( blank=False, null=False, verbose_name='نتیجه یا فرآیند')
    lie = models.CharField(max_length=255, blank=False, null=False, verbose_name='دروغ گفتن')
    g10 = models.SmallIntegerField(blank=False, null=False, verbose_name='جایگاه فعلی شما بر اساس نقاط قوت')

    goodday = models.TextField(blank=False, null=False, verbose_name='روز ایده آل')
    hard = models.TextField(blank=False, null=False, verbose_name='پرچالش ترین')
    hard2 = models.TextField(blank=False, null=False, verbose_name='راهکار اثر بخش')
    age = models.CharField(max_length=255, blank=False, null=False, verbose_name='تیپ سنی')
    gender = models.CharField(max_length=255, blank=False, null=False, verbose_name='تیپ جنسیتی')
    knowlage = models.CharField(max_length=255, blank=False, null=False, verbose_name='تیپ دانش')
    personality = models.CharField(max_length=255, blank=False, null=False, verbose_name='تیپ شخصیتی')

    learning = models.TextField(blank=False, null=False, verbose_name='یادگیری مهارت')
    success = models.TextField(blank=False, null=False, verbose_name='تعریف موفقیت')
    money = models.TextField(blank=False, null=False, verbose_name='دریافت سرمایه')
    g15 = models.SmallIntegerField(blank=False, null=False, verbose_name='رضایت از گذشته')

    creative = models.TextField( blank=False, null=False, verbose_name='خلاق و نوآور')
    leader = models.TextField(blank=False, null=False, verbose_name='رهبری تیم')
    like = models.CharField(max_length=255, blank=False, null=False, verbose_name='علاقه مندی به حرفه خود')
    dislike = models.CharField(max_length=255, blank=False, null=False, verbose_name='عدم علاقه به حرفه خود')

    entrepreneur = models.TextField(blank=False, null=False, verbose_name='ویژگی کارآفرین')
    star = models.TextField(blank=False, null=False, verbose_name='علت ستاره بودن')
    broke = models.TextField(blank=False, null=False, verbose_name='تجربه شکست')
    g17 = models.CharField(max_length=255, blank=False, null=False, verbose_name='مواجهه با چند مساله کاری')
    g18 = models.CharField(max_length=255, blank=False, null=False, verbose_name='مواجعه با مشکل پیچیده')

    suggest = models.TextField(blank=False, null=False, verbose_name='پیشنهاد تغییر')
    area = models.TextField(blank=False, null=False, verbose_name='حوزه فعالیت در آینده')
    newarea = models.TextField(blank=False, null=False, verbose_name='حوزه جدید')
    solution = models.TextField(blank=False, null=False, verbose_name='راه حل مشکل و ضعف')

    is_read = models.BooleanField(default=False, blank=False, null=False, verbose_name='خوانده شده/نشده')

    class Meta:
        verbose_name = 'نظرسنجیها'
        verbose_name_plural = 'نظرسنجی'
        db_table = 'survey'

    def __str__(self):
        return self.fullname


class SurveyStartJob(models.Model):
    unit = models.CharField(max_length=150, blank=False, null=False, verbose_name='واحد شغلی')
    start1 = models.CharField(max_length=10, blank=False, null=False, verbose_name='تاریخ شروع تجارت خارجی')
    end1 = models.CharField(max_length=10, blank=True, null=True, verbose_name='تاریخ پایان تجارت خارجی')
    organ1 = models.CharField(max_length=255, blank=False, null=False, verbose_name='سمت سازماتی تجارت خارجی')
    SR = models.ForeignKey(SurveyResponse, on_delete=models.CASCADE, verbose_name='سمت ها')

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = 'سمت شغلی'
        verbose_name_plural = 'سمت های شغلی'
        db_table = 'surveyjobs'
