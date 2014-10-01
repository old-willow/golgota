from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from medias.models import AudioArchive, VideoArchive


class AudrioArchiveForm(forms.ModelForm):

    class Meta:
        model = AudioArchive
        fields = ('title', 'date_published', 'date_uploaded', 'slug',
                  'active', 'file', 'meeting_leader', )

        def image_clean(self):
            CONTENT_TYPES = ['video', 'audio', ]
            CONTENT_SUBTYPES_AUDIO = ['mpeg', 'x-wav', 'ogg', ]
            CONTENT_SUBTYPES_VIDEO = ['x-msvideo', 'quicktime', 'mpeg', ]

            # 2.5MB - 2621440
            # 5MB - 5242880
            # 10MB - 10485760
            # 20MB - 20971520
            # 50MB - 5242880
            # 100MB 104857600
            # 250MB - 214958080
            # 500MB - 429916160
            # MB - 5242880

            #MAX_UPLOAD_SIZE = '2621440'
            file = self.cleaned_data['file']
            # type
            content_type = content.content_type.split('/')[0]
            subtype = content.content_type.split('/')[1]

            if content_type in CONTENT_TYPES:
                #if content._size > MAX_UPLOAD_SIZE:
                #    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize is %s') %
                #                                (filesizeformat(MAX_UPLOAD_SIZE), (filesizeformat(context._size))))
                if subtype not in CONTENT_SUBTYPES:
                    raise forms.ValidationError(_('Only \'avi\', \'mov\', \'ogg\', \'wav\' and \'mp3\' files allowed!'))

            else:
                raise forms.ValidationError(_('File type not supported.'))
