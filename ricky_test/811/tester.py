#!/usr/bin/python3
# -*- coding: utf-8 -*-
import jinja2

var1 = jinja2.Environment(undefined=jinja2.DebugUndefined).from_string("{{ VAR }}").render({"VAR": "Hello"}) # Should return Hello
var2 = jinja2.Environment(undefined=jinja2.DebugUndefined).from_string("{{ NOVAR }}").render({"VAR": "Hello"}) # Should return {{ NOVAR }}
var3 = jinja2.Environment(undefined=jinja2.DebugUndefined).from_string("{{ NOVAR.items }}").render({"VAR": "Hello"}) # Should return {{ NOVAR.items }}

print(var1)
print(var2)
print(var3)
