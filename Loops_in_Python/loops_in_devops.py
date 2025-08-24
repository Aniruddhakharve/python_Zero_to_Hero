log_file = [   ""
    "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
   ]

for mistake in log_file:
    if "ERROR" in mistake:
        print (mistake)
