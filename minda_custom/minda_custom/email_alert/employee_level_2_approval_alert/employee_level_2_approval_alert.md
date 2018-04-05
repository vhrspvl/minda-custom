<h3>{{_("Employee Creation - Pending Level 2 Approval")}}</h3>

<h4>{{_("Employee Details")}}</h4>
{{_("Employee")}}: {{ frappe.utils.get_link_to_form(doc.doctype, doc.name) }}

{{_("Employee Name")}}: {{ doc.employee_name }}

{{_("Contractor")}}: {{ doc.contractor }}

<h3>Above Employee is Created and Pending for your Approval</h3>

<p>You can Approve by visiting this link {{ frappe.utils.get_link_to_form(doc.doctype, doc.name) }}</p>