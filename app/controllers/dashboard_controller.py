from flask import render_template, flash, session, jsonify
from app.schemas.sell_schema import SellSchema
from app.core.dao.dashboard_dao import DashboardDao
from itertools import repeat
from collections import OrderedDict

class DashboardoController(object):

    def __init__(self):
        self.dao = DashboardDao()

    def sell_per_mark(self):
        data = self.dao.get_sells_per_mark()
        schema = SellSchema(many=True).dump(data)
        return schema

    def sell_by_gender(self):
        data = self.dao.get_sells_by_gender()
        response = dict(
            marks=[],
            series=dict(
                masculino=dict(
                    title='Homem',
                    data=[]
                ),
                feminino=dict(
                    title='Mulher',
                    data=[]
                )
            )
        )
        for i in data:
            response['marks'].append(i[0])
            response['series']['masculino']['data'].append(i[1])
            response['series']['feminino']['data'].append(i[2])
        return response

    def get_sell_by_weekday(self):
        data = self.dao.get_sell_by_weekday()
        categories=['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
        repeat_marks = []
        series = []

        for i in data:
            repeat_marks.append(i.mark)

        marks = list(OrderedDict(zip(repeat_marks, repeat(None))))

        series = {key: dict(name=key, data=list()) for i, key in enumerate(marks)}

        for key, value in series.items():
            for x in range(0, 7):
                value['data'].append(0)

        for key, value in series.items():
            for i in data:
                if key == i.mark:
                    for x in range(0, 7):
                        if x == int(i.dias):
                            value['data'][int(i.dias)] = i.quantidade

        response = dict(
            categories=categories,
            series=[]
        )

        for key, value in series.items():
            response['series'].append(value)

        return response
