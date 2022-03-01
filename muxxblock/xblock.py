from django.conf import settings
from lti_consumer.lti_xblock import LtiConsumerXBlock, _
from xblock.core import Scope, String
from xblockutils.resources import ResourceLoader


class MuxXBlock(LtiConsumerXBlock):
    display_name = String(
        display_name=_("Display Name"),
        help=_(
            "Enter the name that students see for this component. "
            "Analytics reports may also use the display name to identify this component."
        ),
        scope=Scope.settings,
        default=_("Mux video"),
    )
    video_id = String(
        display_name=_("Video ID"),
        default="",
        scope=Scope.settings,
    )
    lti_id = String(
        display_name=_("LTI ID"),
        help=LtiConsumerXBlock.lti_id.help,
        default=getattr(
            settings,
            "LTI_DEFAULT_PASSPORT_ID",
            getattr(settings, "LTI_DEFAULT_MUX_PASSPORT_ID", ""),
        ),
        scope=Scope.settings,
    )
    launch_url = String(
        display_name=_("LTI URL"),
        help=LtiConsumerXBlock.launch_url.help,
        default=getattr(
            settings,
            "LTI_DEFAULT_PRODUCER_LAUNCH_URL",
            "/lti/1.1/launch",
        ),
        scope=Scope.settings,
    )

    # Limit the number of editable fields
    editable_field_names = (
        "display_name",
        "video_id",
        "lti_id",
        "launch_url",
    ) 

    @property
    def prefixed_custom_parameters(self):
        custom_parameters = super().prefixed_custom_parameters
        custom_parameters["custom_app"] = "mux"
        custom_parameters["custom_video_id"] = self.video_id
        return custom_parameters
    
    def student_view(self, context):
        # Override the parent student view to add some custom css
        fragment = super().student_view(context)
        loader = ResourceLoader(__name__)
        fragment.add_css(loader.load_unicode('static/css/muxxblock.css'))
        return fragment
