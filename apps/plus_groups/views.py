from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.db import transaction
from django.utils import simplejson

from apps.hubspace_compatibility.models import TgGroup

from microblogging.models import Following
from apps.plus_lib.models import DisplayStatus, add_edit_key
from apps.plus_permissions.models import SecurityTag
from apps.plus_permissions.interfaces import PlusPermissionsNoAccessException, SecureWrapper
from apps.plus_permissions.types.TgGroup import *
from django.contrib.auth.decorators import login_required


def group(request, group_id, template_name="plus_groups/group.html"):
    group = get_object_or_404(TgGroup, pk=group_id)
    group.save()

    if ps.has_access(request.user,group,ps.get_interface_factory().get_id(TgGroup,'Viewer')) :
        dummy_status = DisplayStatus("Dummy Status"," about 3 hours ago")
        group = NullInterface(group)
        group.load_interfaces_for(request.user)


        return render_to_response(template_name, {
                "head_title" : "%s" % group.display_name,
                "head_title_status" : dummy_status,
                "group" : group,
                "extras" : group.groupextras, 
                }, context_instance=RequestContext(request))

    else :
        return HttpResponse("""
<p>You don't have permission to see or do this.</p>
<p>You are %s</p>
<p>This is the profile for %s via interface %s</p>
Current Permissions
<ul>%s</ul>...""" % (request.user, group.display_name, 'Viewer',
       ''.join([
          ('<li>%s</li>'%x) for x in ps.get_permissions_for(group)
          ]),
       ), status=401 )
