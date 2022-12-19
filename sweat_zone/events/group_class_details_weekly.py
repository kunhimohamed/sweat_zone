
from datetime import date, timedelta
import frappe
from frappe import _

def fetch_customer_group_class_booking_details():
	"""
	fetch customers group class booking details on weekly basis.
	"""
	customers_list = frappe.get_list("Customer")
	for customer in customers_list:
		group_class_book_details = group_class_book_details_method(customer.name)
		if group_class_book_details:
			table_row_data = make_table_row(group_class_book_details)
			final_table = create_final_table(table_row_data)
			customer_email_id = get_customer_email_id(customer.name)
			if customer_email_id:
				email_id = customer_email_id
				email_args = {
					"recipients": [email_id],
					"message": _(final_table),
					"subject": 'Booked Class Summary From Sweat Zone'
					}
				frappe.sendmail(**email_args)

def get_customer_email_id(customer_name):
	"""
	Get customer email id
	"""
	customer_email_id = frappe.db.sql("""
				select 
					tc.email_id  
				from 
					`tabDynamic Link` tdl
				join 
					tabContact tc 
				on 
					tc.name=tdl.parent 
				where 
					tdl.link_name = '{customer_name}';
			""".format(customer_name=customer_name), as_dict=1)
	if customer_email_id:
		return customer_email_id[0].get("email_id")

def group_class_book_details_method(cusomer_name):
	"""
	fetch booked class details
	"""
	today = date.today()
	week_start = today - timedelta(days=today.weekday())
	week_end = week_start + timedelta(days=6)
	group_class_book_details = frappe.db.sql("""
			select 
				tgcbd.name, tgcbd.group_class, tgcbd.date, tbgc.customer, tgcbd.comment  
			from 
				`tabBook Group Class` tbgc 
			join 
				`tabGroup Class Book Detail` tgcbd 
			on 
				tgcbd.parent = tbgc.name
			where 
				tgcbd.date>='{week_start}' and tgcbd.date<='{week_end}' and tbgc.customer='{customer_name}'
			group by tgcbd.date;
		""".format(week_start=week_start, week_end=week_end, customer_name=cusomer_name), as_dict=1)
	return group_class_book_details

def make_table_row(group_class_details):
	"""
	make table row with details
	"""
	tbody_row = ""
	for group_detail in group_class_details:
		group_class_from_group_detail = str(group_detail.get("group_class")) if group_detail.get("group_class") else ""
		group_class = '<td>'+group_class_from_group_detail+'</td>'
		comment_from_group_detail = str(group_detail.get("comment")) if group_detail.get("comment") else ""
		comment = "<td>"+comment_from_group_detail+"</td>"
		booked_date_from_group_detail = str(group_detail.get("date")) if group_detail.get("date") else ""
		booked_date = "<td>"+booked_date_from_group_detail+"</td>"
		row = "<tr>\
		{group_class}\
		{comment}\
		{booked_date}\
			</tr>".format(
			group_class = group_class,
			comment = comment,
			booked_date = booked_date
		)
		tbody_row += row
	return tbody_row

def create_final_table(tbody_row):
	"""
	create final table
	"""
	final_table = """<table class="table table-striped thead-default table-bordered">\
				<thead>
				<tr>
					<th>Group Class</th>
					<th>Comment</th>
					<th>Booked Date</th>
				</tr>
				</thead>
				<tbody>
				{row_body}
				</tbody>
			</table>""".format(row_body=tbody_row)
	return final_table

