from app import app
from datetime import datetime
from app.models.return_itens import ReturnItens
from app.controllers.return_itens_controller import ReturnItensController
from app.controllers.order_controller import OrderController
from flask import redirect, render_template, url_for, Flask, request, flash, session
from flask_login import login_required

@app.route('/confirm_return', methods=['POST'])
@login_required
def confirm_return():
    order_id = request.form.get('order_id')
    itens = request.form.get('itens').split(',')
    if request.form.get('option-text') == '':
        reason = request.form.get('option')
    else:
        reason = request.form.get('option-text')
    for item in itens:
        obj = ReturnItens(
            item_id=int(item),
            order_id=order_id,
            reason=reason,
            item_quantity=int(request.form.get('item_quantity')),
            item_value=float(request.form.get('item_value')),
            status='Aguardando aprovação do administrador',
            created_at=datetime.today(),
            updated_at=datetime.today()
        )
        result = ReturnItensController.request_return(obj)
    flash('Devolução de produtos solicitada!')
    return redirect('/buy_details/'+order_id)


@app.route('/return_items', methods=['POST'])
@login_required
def select_items_return():
    itens_list = ','.join(request.form.getlist('selected_itens'))
    order_id = request.form.get('order_id')
    item_quantity = int(request.form.get('quantity'))
    item_value = float(request.form.get('item_value'))
    if request.form.get('botao') == 'return':
        return render_template('operations/confirm_return.html.j2',
                itens=itens_list,
                order_id=order_id,
                item_quantity=item_quantity,
                item_value=item_value * item_quantity
            )
    else:
        if not 'beer' in session['cart'] or not 'snack' in session['cart']:
            return 'Por favor, insira itens no carrinho para que possamos efetuar a troca!'

@app.route('/admin/returns', methods=['POST', 'GET'])
@login_required
def returns():
    if request.method == 'GET':
        returns = ReturnItens.query.all()
        return render_template('operations/returns.html.j2', returns=returns)
    else:
        order = dict(
            return_id=int(request.form.get('return_id')),
            id=int(request.form.get('order_id')),
            value=float(request.form.get('value')),
            quantity=request.form.get('quantity'),
            item_id=request.form.get('item_id')
        )
        client_id = request.form.get('client_id')

        result = OrderController.update(order, client_id)

        ReturnItensController.confirmed_returned(order['item_id'])
        flash('Devolução de produto confirmada!')
        return redirect(request.referrer)
