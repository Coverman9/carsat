# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from datetime import date
# from wtforms.fields import DateField
# from wtforms.fields import DateTimeField


# @app.route('/dateExample',methods=['GET','POST'])
#     def index():
#         error = None
#         form = TestForm()
#         if form.validate_on_submit():
#             return 'Start Date is : {} End Date is : {}'.format(form.startdate.data, form.enddate.data)
#         else:
#             error = "Start date is greater than End date"
#         return render_template('dateExample.html',form=form,error = error)
