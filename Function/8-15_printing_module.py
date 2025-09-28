#1
import printing_models
printing_models.models('arya','kumar','sridevi','chitrlekha')

#2
from printing_models import models

models('arya','kumar','sridevi','chitrlekha')

#3
from printing_models import models as mo1

mo1('arya','kumar','sridevi','chitrlekha')

#4
import printing_models as pm

pm.models('arya','kumar','sridevi','chitrlekha')

#5
from printing_models import *

models('arya','kumar','sridevi','chitrlekha')