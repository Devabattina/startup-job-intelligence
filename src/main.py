from job_data import jobs
from email_sender import send_email

html = """
<h2>Daily Job Report</h2>

<table border="1" cellpadding="5">
<tr>
<th>Company</th>
<th>Role</th>
<th>Location</th>
<th>Experience</th>
<th>Apply</th>
</tr>
"""

for job in jobs:
    html += f"""
    <tr>
        <td>{job['company']}</td>
        <td>{job['role']}</td>
        <td>{job['location']}</td>
        <td>{job['experience']}</td>
        <td><a href="{job['apply_link']}">Apply</a></td>
    </tr>
    """

html += "</table>"

send_email(html)

print("Job Report Sent")