# -*- coding: utf-8 -*-
"""
Create Time: 2021/6/21 5:34 下午
Author: Aries
"""
from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired

class  SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])   #列表可以传入多个校验规则
    #验证器后面可以传message   DataRequired校验有效性 过滤空格等操作
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
