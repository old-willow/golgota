from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from home.models import Staff, STAFFTITLES


class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'nickname', 'slug', 'image',
                  'image_publishable', 'email', 'email_publishable', 'web',
                  'web_publishable', 'fb_profile', 'fb_publishable',
                  'mob_phone', 'mob_phone_publishable', 'phone', 'phone_publishable',
                  'title', 'about_me', 'date_registered', )
        widgets = {
            'title': forms.CheckboxSelectMultiple,
        }
        labels = {
            'title': _('Title'),
        }

        def image_clean(self):
            #CONTENT_TYPES = ['image', 'video', 'audio', ]
            CONTENT_TYPES = ['image', ]
            # Accepted content types: image/gif; image/jpg; image/png
            CONTENT_SUBTYPES = ['jpg', 'png', 'gif',  ]

            # 2.5MB - 2621440
            # 5MB - 5242880
            # 10MB - 10485760
            # 20MB - 20971520
            # 50MB - 5242880
            # 100MB 104857600
            # 250MB - 214958080
            # 500MB - 429916160
            # MB - 5242880

            MAX_UPLOAD_SIZE = '2621440'
            image = self.cleaned_data['image']
            # type
            content_type = content.content_type.split('/')[0]
            subtype = content.content_type.split('/')[1]

            if content_type in CONTENT_TYPES:
                if content._size > MAX_UPLOAD_SIZE:
                    raise forms.ValidationError(_('Please keep filesize under %(bytes)s. Current filesize is %(currsize)s') %
                                                (filesizeformat(MAX_UPLOAD_SIZE), (filesizeformat(context._size))))
                if subtype not in CONTENT_SUBTYPES:
                    raise forms.ValidationError(_('Only \'jpg\', \'gif\' and \'png\' image files allowed!'))

            else:
                raise forms.ValidationError(_('File type not supported.'))
