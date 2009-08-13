
# Permissions for OurPost, an example 

from django.db import models

from models import Interface, Slider, SecurityTag, PermissionManager
from models import InterfaceReadProperty, InterfaceWriteProperty
from models import get_permission_system, default_admin_for, PermissionableMixin

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from permissionable import *

from apps.hubspace_compatibility.models import TgGroup

import ipdb

# This represents a typical model type from another django or pinax app

class OurPost(PermissionableMixin, models.Model):
    title = models.CharField(max_length='20')
    body = models.CharField(max_length='20')

    def __str__(self):
        return "OurPost %s,%s" % (self.title,self.body)

    def foo(self):
        pass


# Here's the wrapping we have to put around it.

class OurPostViewer: 
    title = InterfaceReadProperty
    body = InterfaceReadProperty

class OurPostEditor: 
    title = InterfaceWriteProperty
    body = InterfaceWriteProperty
    delete = InterfaceCallProperty

class OurPostCommentor:
    pass


from apps.plus_permissions.interfaces import interface_map

OurPostInterfaces = {'Viewer':OurPostViewer,
                     'Editor':OurPostEditor,
                     'Commentor':OurPostCommentor}

add_type_to_interface_map(OurPost, OurPostInterfaces)

