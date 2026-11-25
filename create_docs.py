import fitz  # PyMuPDF - you already have it
import os

os.makedirs("docs", exist_ok=True)

def make_pdf(filename, title, content):
    doc = fitz.open()
    page = doc.new_page()
    # Title
    page.insert_text((50, 50), title, fontsize=20, fontname="helv")
    # Body - split into lines
    y = 90
    for line in content.split("\n"):
        if y > 750:
            page = doc.new_page()
            y = 50
        # Wrap long lines
        if len(line) > 95:
            # split
            for i in range(0, len(line), 95):
                page.insert_text((50, y), line[i:i+95], fontsize=11, fontname="helv")
                y += 16
        else:
            page.insert_text((50, y), line, fontsize=11, fontname="helv")
            y += 16
        if line == "":
            y += 6
    doc.save(f"docs/{filename}")
    print(f"Created docs/{filename}")

# DOC 1: Payroll
make_pdf("PeopleSoft_Payroll_Manual.pdf", "PeopleSoft Payroll Manual - v12.1", """
1. PAYROLL CUTOFF PROCESS
The payroll cutoff for all US employees is the 15th and 30th of each month at 5:00 PM PST.
All timesheets must be approved by managers before cutoff.
Late timesheets will be processed in the next payroll cycle. No exceptions without HR Director approval.

Timesheet approval flow:
1. Employee submits timesheet by 12:00 PM on cutoff day
2. Manager approves by 3:00 PM on cutoff day
3. HR reviews by 5:00 PM on cutoff day

Overtime is calculated at 1.5x for hours over 40 per week.
Contractors are paid on Net-30 terms, not in bi-monthly payroll.

2. LEAVE POLICY FOR CONTRACTORS
Contractors do not accrue PTO. They must notify their manager 2 weeks in advance for planned leave.
Unplanned leave must be reported by 9:00 AM on the day of absence.
Contractors are not eligible for paid holidays.
""")

# DOC 2: Procurement
make_pdf("SAP_Vendor_Management.pdf", "SAP Vendor Management Guide", """
1. HOW TO CREATE A NEW VENDOR
To create a new vendor in SAP:
Step 1: Go to Transaction XK01
Step 2: Enter Vendor Group: ZDOM for domestic, ZINT for international
Step 3: Enter Company Code: 1000 for US, 2000 for EU
Step 4: Enter Tax ID and Bank Details. Bank details are mandatory.
Step 5: Submit for approval. Finance Manager must approve within 48 hours.

Vendor will be BLOCKED until Finance approval is complete.
Duplicate check is done on Tax ID. If Tax ID exists, system will show error: Vendor Already Exists.

2. APPROVAL LEVELS FOR EXPENSE
Expense approval levels:
- Under $500: Manager approval only
- $500 to $5000: Manager + Finance Manager approval
- $5000 to $25000: Manager + Finance Manager + Director approval
- Over $25000: Requires VP approval + Procurement Committee

All expenses over $5000 require 2 quotes from vendors.
Travel expenses must be submitted within 15 days of travel.
""")

# DOC 3: Finance Close
make_pdf("Oracle_Month_End_Close.pdf", "Oracle Month-End Close Procedure", """
1. HOW TO RUN MONTH-END CLOSE
Month-end close must be completed by the 3rd business day of next month.

Close checklist:
Day 1: Close AP and AR subledgers. Run Reconciliation Report.
Day 2: Post all journal entries. Run Trial Balance.
Day 3: Review variances over $10,000. CFO signs off.

If variance is over $10,000, do not close. Escalate to Finance Controller immediately.

2. EXPENSE REIMBURSEMENT
Employees must submit receipts for all expenses over $25.
Reimbursement is processed on Fridays only.
Direct deposit is the only payment method. No checks.

3. VENDOR PAYMENT TERMS
Standard payment terms: Net-30.
Early payment discount: 2% if paid within 10 days (2/10 Net 30).
International vendors: Net-45.
""")

print("\nDone! 3 docs created in docs/ folder")