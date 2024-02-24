from django.test import TestCase
import json
import markdown2

# Create your tests here.
st=None

res=json.dumps(st)
res2=markdown2.markdown(st)
print(res,"  ",res2)