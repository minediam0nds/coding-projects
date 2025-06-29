 
#INFOCOMM = INF | NPCC = NPC | FLOORBALL = FLO |

CCA_budgets = [0, 0, 0]
CCA_expenses = ["INF", 1 , 1 , 2024 , 1230 , 6200 , "DEFAULT ALLOCATION" , "FLO" , 1 , 1 , 2024 , 1200 , 5000 , "DEFAULT ALLOCAtION" , "NPC" , 1 , 1 , 2024 , 1200 , 5000 , "DEFAULT ALLOCATION" ,\
                "FLO" , 2, 1 , 2024 , 1030 , -500 , "floorball sticks" , "INF" , 2 , 1 , 2024 , 1159 , -2000 , "Computer" , "NPC" , 3 , 1 , 2024 , 1159 , -150 , "Uniforms"]
selectedcca = 0
selectedccaname = ""
selectedccaid = 0
infallocated = False
npcallocated = False
floallocated = False
def chatbot():
    while True:
        print("Welcome to the Chatbot")
        print("Please choose an option to learn more:")
        print("----------------------------------------------------------------")
        print("1. How to use the Add Expense function.")
        print("2. How to use the Delete Expense function.")
        print("3. How to use the Amend Expense function.")
        print("4. How to use the View Expenses function.")
        print("5. How to start Budget Allocation for all CCAs.")
        print("6. How to check our current budget.")
        print("7. How to fix a mistyped expense.")
        print("8. Exit & Return to menu")
        print("----------------------------------------------------------------")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print("To use the Add Expense function:\n"
                  "1. Select 'Add Expenses' from the menu.\n"
                  "2. Choose the CCA (Infocomm, NPCC, or Floorball) for which you want to add an expense.\n"
                  "3. Enter the expense details including the date, time, amount, and reason.\n"
                  "4. Ensure that the amount does not exceed the allocated budget for that CCA.\n"
                  "5. The expense will be recorded and reflected in the respective CCA's expenses.")

        elif choice == "2":
            print("To use the Delete Expense function:\n"
                  "1. Select 'Delete Expenses' from the menu.\n"
                  "2. Choose the CCA (Infocomm, NPCC, or Floorball) for which you want to delete an expense.\n"
                  "3. Review the list of expenses and select the one you wish to delete.\n"
                  "4. Confirm the deletion, and the expense will be removed from the record.")

        elif choice == "3":
            print("To use the Amend Expense function:\n"
                  "1. Select 'Amend Expenses' from the menu.\n"
                  "2. Choose the CCA (Infocomm, NPCC, or Floorball) for which you want to amend an expense.\n"
                  "3. Find the expense you want to amend and enter the new details.\n"
                  "4. Confirm the changes, and the expense details will be updated.")

        elif choice == "4":
            print("To use the View Expenses function:\n"
                  "1. Select 'View Expenses' from the menu.\n"
                  "2. Choose the CCA (Infocomm, NPCC, or Floorball) whose expenses you want to view.\n"
                  "3. Review the list of expenses displayed, which includes the date, time, amount, and reason.")

        elif choice == "5":
            print("To start Budget Allocation for all CCAs:\n"
                  "1. Select 'Allocate Budget' from the menu.\n"
                  "2. Choose the CCA for which you want to allocate the budget.\n"
                  "3. Enter the date and amount to allocate.\n"
                  "4. Confirm the allocation, and the budget will be updated accordingly.")

        elif choice == "6":
            print("To check your current budget:\n"
                  "1. Select 'View Budgets' from the menu.\n"
                  "2. Review the current budget allocation for each CCA (Infocomm, NPCC, Floorball).\n"
                  "3. The displayed amounts represent the available budget for each CCA.")

        elif choice == "7":
            print("To fix a mistyped expense:\n"
                  "1. Select 'Amend Expenses' from the menu.\n"
                  "2. Choose the CCA and find the expense you want to correct.\n"
                  "3. Enter the correct details and save the changes.\n"
                  "4. The expense record will be updated with the corrected information.")

        elif choice == "8":
            print("Exiting the chatbot. Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 8.")
def spaced():
  print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
  print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


def searchexpense():
    global set_chosen_cca
    global selectedcca3letters
    global CCA_expenses
    global selectedccaname
    global selectedccaid

    print("---------------------------------")
    print("|       SEARCHING EXPENSES      |")
    print("---------------------------------")
    while True:

      while True:

        print("Select CCA to search expenses")
        print("1. Infocomm")
        print("2. NPCC")
        print("3. Floorball")
        print("4. Exit & return to main menu")
        ccachoice = input("Enter choice (1-4): ")

        if ccachoice in ["1", "2", "3", "4"]:
          break
        else:
            print("------------------")
            print("| INVALID INPUT  |")
            print("------------------")

      if ccachoice == "4":
          print("---------------------------------")
          print("|       RETURNING TO MENU       |")
          print("---------------------------------")
          return

      if ccachoice == "1":
          selectedcca = "INF"
          selectedccaname = "Infocomm"
          selectedccaid = 1
          selectedcca3letters = "INF"
      elif ccachoice == "2":
          selectedcca = "NPC"
          selectedccaname = "NPCC"
          selectedccaid = 2
          selectedcca3letters = "NPC"
      elif ccachoice == "3":
          selectedcca = "FLO"
          selectedccaname = "Floorball"
          selectedccaid = 3
          selectedcca3letters = "FLO"


      while True:
          print("--------------------------------------------------------")
          print("| SEARCHING EXPENSES FOR " + selectedccaname + " |")
          print("--------------------------------------------------------")
          print("Choose parameters to search by:")
          print("1. Date")
          print("2. Amount")
          print("3. Reason")
          print("4. Exit & return to main menu")
          searchchoice = input("Enter choice (1-7): ")
          if searchchoice in ["1", "2" , "3" , "4"]:
              break
          else:
              print("------------------")
              print("| INVALID INPUT  |")
              print("------------------")

      if searchchoice == "4":
          print("---------------------------------")
          print("|       RETURNING TO MENU       |")
          print("---------------------------------")
          return

      if searchchoice == "1":
        while True:
          print("--------------------------------------------------------")


          print("Enter date to begin search")
          searchday = input("Enter day: ")
          searchmonth = input("Enter month: ")
          searchyear = input("Enter year: ")
          selectedcca3letters = selectedcca[:3]
          if searchday.isdigit() and searchmonth.isdigit() and searchyear.isdigit():
            break
          else:
            print("------------------")
            print("| INVALID INPUT  |")
            print("------------------")

        print("SHOWING RESULTS FOR (" + searchday + " " + searchmonth + " " + searchyear + ")")
        print("_________________________________________________________________________")
        print("Day   Month   Year    Time    Amount     Reason")

        searchexpenseexist = False
        for i in range(len(CCA_expenses)):
            if (i + 6 ) < len(CCA_expenses):

              if CCA_expenses[i] == selectedcca3letters and CCA_expenses[i + 1] == int(searchday) and CCA_expenses[i + 2] == int(searchmonth) and  CCA_expenses[i + 3] == int(searchyear):
                searchexpenseexist = True
                day = CCA_expenses[i + 1]
                month = CCA_expenses[i + 2]
                year = CCA_expenses[i + 3]
                time = CCA_expenses[i + 4]
                amount = CCA_expenses[i + 5]
                reason = CCA_expenses[i + 6]
                if int(amount) < 0:
                  print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
                else:

                  print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")

        if not searchexpenseexist:
            print(" No expenses found for the given date.")

        print("_________________________________________________________________________")



      elif searchchoice == "2":
        searchexpenseexist = False
        while True:
          print("--------------------------------------------------------")
          print("Enter amount to begin search")
          searchamount = input("Enter amount: ")
          if searchamount.isdigit():
            break
          else:
            print("------------------")
            print("| INVALID INPUT  |")
            print("------------------")
        print("SHOWING RESULTS FOR (" + searchamount + ")")
        print("_________________________________________________________________________")
        print("Day   Month   Year    Time    Amount     Reason")

        for i in range(len(CCA_expenses)):
          if (i + 6 ) < len(CCA_expenses):
            if CCA_expenses[i] == selectedcca3letters and CCA_expenses[i + 5] == (searchamount):
              searchexpenseexist = True
              day = CCA_expenses[i + 1]
              month = CCA_expenses[i + 2]
              year = CCA_expenses[i + 3]
              time = CCA_expenses[i + 4]
              amount = CCA_expenses[i + 5]
              reason = CCA_expenses[i + 6]
              if int(amount) < 0:
                print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
              else:
                print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")
        if not searchexpenseexist:
            print(" No expenses found for the given reason.")

        print("_________________________________________________________________________")



      elif searchchoice == "3":
        searchexpenseexist = False
        print("--------------------------------------------------------")
        print("Enter reason to begin search")
        searchreason = input("Enter reason: ")
        print("SHOWING RESULTS FOR (" + searchreason + ")")
        print("_________________________________________________________________________")
        print("Day   Month   Year    Time    Amount     Reason")
        for i in range(len(CCA_expenses)):
          if (i + 6 ) < len(CCA_expenses):
            if CCA_expenses[i] == selectedcca3letters and searchreason in CCA_expenses[i + 6]:
              searchexpenseexist = True
              day = CCA_expenses[i + 1]
              month = CCA_expenses[i + 2]
              year = CCA_expenses[i + 3]
              time = CCA_expenses[i + 4]
              amount = CCA_expenses[i + 5]
              reason = CCA_expenses[i + 6]
              if int(amount) < 0:
                print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
              else:
                print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")
        if not searchexpenseexist:
            print(" No expenses found for the given reason.")

        print("_________________________________________________________________________")








def setbudget():
  global CCA_expenses
  global CCA_budgets
  infamount = 0
  npcamount = 0
  floamount = 0
  for i in range(len(CCA_expenses)):
    if CCA_expenses[i] == "INF":
      infamount += int(CCA_expenses[i + 5])
    if CCA_expenses[i] == "NPC":
      npcamount += int(CCA_expenses[i + 5])
    if CCA_expenses[i] == "FLO":
      floamount += int(CCA_expenses[i + 5])
  CCA_budgets[0] = infamount
  CCA_budgets[1] = npcamount
  CCA_budgets[2] = floamount

def amendexpense():
    global setbudget
    global CCA_expenses
    global CCA_budgets
    global set_chosen_cca
    global selectedccaname
    global selectedccaid
    setbudget()
    print("---------------------------------")
    print("|       AMENDING EXPENSES       |")
    print("---------------------------------")

    while True:
        print("Select CCA to amend expense")
        print("1. Infocomm")
        print("2. NPCC")
        print("3. Floorball")
        print("4. Exit & return to main menu")
        ccachoice = input("Enter choice(1-4): ")

        if ccachoice in ["1", "2", "3", "4"]:
            break
        else:
            print("------------------")
            print("| INVALID INPUT  |")
            print("------------------")

    if ccachoice in ["1", "2", "3"]:
        set_chosen_cca(ccachoice)

    if ccachoice == "4":
        print("---------------------------------")
        print("|       RETURNING TO MENU       |")
        print("---------------------------------")
        return

    print("--------------------------------------------------------")
    print("| VIEWING EXPENSES FOR " + selectedccaname + " |")
    print("--------------------------------------------------------")
    print("No. Day   Month   Year    Time    Amount     Reason")
    print("________________________________________________________________________________")

    expensenotexist = True
    idcount = 0

    for i in range(len(CCA_expenses)):
        if (selectedccaid == 1 and CCA_expenses[i] == "INF") or \
           (selectedccaid == 2 and CCA_expenses[i] == "NPC") or \
           (selectedccaid == 3 and CCA_expenses[i] == "FLO"):
            if i + 6 < len(CCA_expenses):
                idcount += 1
                day = CCA_expenses[i + 1]
                month = CCA_expenses[i + 2]
                year = CCA_expenses[i + 3]
                time = CCA_expenses[i + 4]
                amount = CCA_expenses[i + 5]
                reason = CCA_expenses[i + 6]
                expensenotexist = False
                print(f"{idcount} {day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")

    if expensenotexist:
        print("No existing expenses for " + selectedccaname)
        print("________________________________________________________________________________")
        return

    while True:
        print("Choose No. of expense to amend")
        choice = input("Enter choice(1-" + str(idcount) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= idcount:
            choice = int(choice)
            break
        else:
            print("Invalid input, try again")

    expense_index = 0
    for i in range(len(CCA_expenses)):
        if (selectedccaid == 1 and CCA_expenses[i] == "INF") or \
           (selectedccaid == 2 and CCA_expenses[i] == "NPC") or \
           (selectedccaid == 3 and CCA_expenses[i] == "FLO"):
            if expense_index == choice - 1:
                amendindex = i
                day = CCA_expenses[i + 1]
                month = CCA_expenses[i + 2]
                year = CCA_expenses[i + 3]
                time = CCA_expenses[i + 4]
                amount = CCA_expenses[i + 5]
                reason = CCA_expenses[i + 6]
                print("---------------------------------")
                print("|       AMENDING EXPENSE        |")
                print("---------------------------------")
                while True:
                    print("Current details:")
                    print(f"Day: {day}")
                    print(f"Month: {month}")
                    print(f"Year: {year}")
                    print(f"Time: {time}")
                    print(f"Amount: {amount}")
                    print(f"Reason: {reason}")

                    # Amend details
                    new_day = input("Enter new Day (leave blank to keep current): ")
                    new_month = input("Enter new Month (leave blank to keep current): ")
                    new_year = input("Enter new Year (leave blank to keep current): ")
                    new_time = input("Enter new Time (leave blank to keep current): ")
                    new_amount = input("Enter new amount, enter (-) or (+) for spending or adding (leave blank to keep current): ")
                    new_reason = input("Enter new Reason (leave blank to keep current): ")

                    # Default to current values if input is blank
                    if new_day == "":
                        new_day = day
                    if new_month == "":
                        new_month = month
                    if new_year == "":
                        new_year = year
                    if new_time == "":
                        new_time = time
                    if new_amount == "":
                        new_amount = amount
                    if new_reason == "":
                        new_reason = reason

                    # Validate and update the expense
                    try:
                        new_day = int(new_day)
                        new_month = int(new_month)
                        new_year = int(new_year)
                        new_time = int(new_time)
                        new_amount = int(new_amount)

                        if (1 <= new_day <= 31) and (1 <= new_month <= 12) and (len(str(new_year)) == 4) and (0 <= new_time < 2400):
                            if CCA_budgets[selectedccaid - 1] - new_amount >= 0:
                                new_amount = new_amount
                                CCA_expenses[amendindex + 1] = new_day
                                CCA_expenses[amendindex + 2] = new_month
                                CCA_expenses[amendindex + 3] = new_year
                                CCA_expenses[amendindex + 4] = new_time
                                CCA_expenses[amendindex + 5] = new_amount
                                CCA_expenses[amendindex + 6] = new_reason
                                print("Expense amended successfully.")
                                break
                            else:
                                print("New amount would exceed budget, try again")
                        else:
                            print("Inputs do not make sense")
                    except ValueError:
                        print("Invalid inputs")

                break
            expense_index += 1









def deleteexpense():
    global setbudget
    global CCA_expenses
    global CCA_budgets
    global selectedccaid
    global selectedccaname

    while True:
        print("---------------------------------")
        print("|       DELETING EXPENSES       |")
        print("---------------------------------")
        print("Select CCA to delete expense")
        print("1. Infocomm")
        print("2. NPCC")
        print("3. Floorball")
        print("4. Exit & return to main menu")
        ccachoice = input("Enter choice(1-4): ")

        if ccachoice in ["1", "2", "3", "4"]:
            break
        else:
            print("------------------")
            print("| INVALID INPUT  |")
            print("------------------")

    if ccachoice == "4":
        print("---------------------------------")
        print("|       RETURNING TO MENU       |")
        print("---------------------------------")
        return

    set_chosen_cca(ccachoice)

    print("---------------------------------")
    print("| VIEWING EXPENSES FOR " + selectedccaname + " |")
    print("---------------------------------")
    print("No. Day   Month   Year    Time    Amount     Reason")
    print("________________________________________________________________________________")

    expensenotexist = True
    idcount = 0
    expense_indexes = []

    for i in range(len(CCA_expenses)):
        if (selectedccaid == 1 and CCA_expenses[i] == "INF") or \
           (selectedccaid == 2 and CCA_expenses[i] == "NPC") or \
           (selectedccaid == 3 and CCA_expenses[i] == "FLO"):
            if i + 6 < len(CCA_expenses):
                expense_indexes.append(i)
                idcount += 1
                day = CCA_expenses[i + 1]
                month = CCA_expenses[i + 2]
                year = CCA_expenses[i + 3]
                time = CCA_expenses[i + 4]
                amount = CCA_expenses[i + 5]
                reason = CCA_expenses[i + 6]
                expensenotexist = False
                print(f"{idcount} {day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")

    if expensenotexist:
        print("No existing expenses for " + selectedccaname)
        print("________________________________________________________________________________")
        return

    print("________________________________________________________________________________")
    while True:
        print("Choose No. of expense to delete")
        choice = input("Enter choice(1-" + str(idcount) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= idcount:
            choice = int(choice)
            break
        else:
            print("Invalid input, try again")

    expense_index = expense_indexes[choice - 1]  # Adjust for zero-based index

    # Retrieve the amount of the expense to be deleted
    expense_amount = int(CCA_expenses[expense_index + 5])
    budget_index = selectedccaid - 1  # Adjust for zero-based index

    # Calculate the new budget after the deletion
    new_budget = CCA_budgets[budget_index] - expense_amount

    # Check if deleting this expense would keep the budget non-negative
    if new_budget < 0:
        print("Deleting this expense would exceed the budget for " + selectedccaname + ".")
        return

    # Proceed to delete the expense
    for _ in range(7):  # Remove the 7 elements for the selected expense
        CCA_expenses.pop(expense_index)
    CCA_budgets[budget_index] = new_budget  # Update the budget
    print("Expense deleted successfully.")









def addexpense(name, day , month , year , time , amount1 , reason ):

  global CCA_expenses
  CCA_expenses.append(name)
  CCA_expenses.append(day)
  CCA_expenses.append(month)
  CCA_expenses.append(year)
  CCA_expenses.append(time)
  CCA_expenses.append(amount1)
  CCA_expenses.append(reason)
  return
def budgetpossible(id):
  infbudget = 0
  npcbudget = 0
  flobudget = 0
  infbudgetpossible = True
  npcbudgetpossible = True
  flobudgetpossible = True
  global CCA_budgets
  if len(CCA_expenses) >= 7:
         for i in range(len(CCA_expenses)):
            if CCA_expenses[i] == "INF":
              expense = CCA_exppenses[i + 5]
              infbudget += expense
         if CCA_budget[0] - infbudget < 0:
          infbudgetpossible = False

         for i in range(len(CCA_expenses)):
            if CCA_expenses[i] == "NPC":
              expense = CCA_exppenses[i + 5]
              npcbudget += expense
         if CCA_budget[1] - npcbudget < 0:
          npcbudgetpossible = False

         for i in range(len(CCA_expenses)):
            if CCA_expenses[i] == "FLO":
              expense = CCA_exppenses[i + 5]
              flobudget += expense
         if CCA_budget[2] - flobudget < 0:
          flobudgetpossible = False
  else:
    quit()
  if infbudgetpossible and npcbudgetpossible and flobudgetpossible:
    return True
  else:
    return False
def addexpenses():
  global CCA_expenses
  global setbudget
  global selectedccaname
  global selectedccaid
  print("---------------------------------")
  print("|       ADDING EXPENSES         |")
  print("---------------------------------")
  while True:

    setbudget()
    print("Select CCA to add expense")
    print("1. Infocomm")
    print("2. NPCC")
    print("3. Floorball")
    print("4. Exit & return to main menu")
    ccachoice = input("Enter choice(1-4): ")
    if ccachoice in ["1", "2", "3", "4"]:
      break
    else:
      print("------------------")
      print("| INVALID INPUT  |")
      print("------------------")
  if ccachoice == "4":
    print("---------------------------------")
    print("|       RETURNING TO MENU       |")
    print("---------------------------------")
    return
  elif ccachoice in ["1", "2", "3"]:
    set_chosen_cca(ccachoice)
    if selectedccaid ==  1:
      letter = "INF"
    elif selectedccaid == 2:
      letter = "NPC"
    elif selectedccaid == 3:
      letter = "FLO"
    print("---------------------------------------------")
    print(" ADDING EXPENSES FOR " + selectedccaname + " ")
    print("---------------------------------------------")
    while True:
      print("Enter expense details")
      day = input("Enter day: ")
      month = input("Enter month: ")
      year = input("Enter year: ")
      time = input("Enter time: ")
      amount = input("Enter amount: ")
      reason = input("Enter reason: ")
      if day.isdigit() and month.isdigit() and year.isdigit() and time.isdigit() and amount.isdigit():
        if int(day) > 0 and int(month) > 0 and int(year) > 0 and int(time) > -1 and int(amount) > 0 and \
        int(day) < 32 and int(month) < 13 and len(str(year)) == 4 and int(time) < 2400:
            if (selectedccaid == 1 and CCA_budgets[0] - int(amount) >= 0) or \
                (selectedccaid == 2 and CCA_budgets[1] - int(amount) >= 0) or \
                (selectedccaid == 3 and CCA_budgets[2] - int(amount) >= 0):

                amount = int(amount)

                addexpense(letter, int(day), int(month), int(year), int(time), int(amount), reason)
                print("Added expense")
                print("________________________________________________________________________________")
                print("Day   Month   Year    Time    Amount     Reason")
                print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
                print("________________________________________________________________________________")
                print("________________________________________________________________________________")
                break
            else:
              print("Budget exceeded, try again")
        else:
          print("------------------")
          print("| INVALID INPUT  |")
          print("------------------")

      else:
        print("------------------")
        print("| INVALID INPUT digit |")
        print("------------------")



def allocatebudget():
    global infallocated
    global npcallocated
    global floallocated
    global CCA_budgets
    print("---------------------------------")
    print("|      ALLOCATING BUDGETS       |")
    print("---------------------------------")

    while True:
        print("Select CCA to allocate budget")
        if infallocated == False:
            print("1. Infocomm ")
        else:
            print("1. Infocomm (allocated)")
        if npcallocated == False:
            print("2. NPCC")
        else:
            print("2. NPCC (allocated)")
        if floallocated == False:
            print("3. Floorball")
        else:
            print("3. Floorball (allocated)")
        print("4. Exit & return to main menu")
        allocatechoice = input("Enter choice(1-4): ")

        if allocatechoice == "1":
            while True:
                print("Allocating budget for Infocomm")
                print("---------------------------------")
                print("Date:")
                day = input("Enter day: ")
                month = input("Enter month: ")
                year = input("Enter year: ")
                time = input("Enter time: ")
                if day.isdigit() and month.isdigit() and year.isdigit() and time.isdigit():
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    time = int(time)
                    if day > 0 and month > 0 and year > 0 and len(str(year)) == 4 and time > 0 and len(str(time)) == 4:
                        if day < 32 and month < 13:
                            if time < 2400:
                              day = int(day)
                              month = int(month)
                              year = int(year)
                              time = int(time)
                              break
                print("One or more inputs wrong, try again")
            while True:
                amountallocated = input("Enter amount to allocate: ")
                if amountallocated.isdigit() and int(amountallocated) > 0:
                    break
                print("Invalid input, try again")
            addexpense("INF", day, month, year, time, amountallocated , "Allocation")
            print("Infocomm budget allocated (" + str(amountallocated) + ")")
            print("------------------------------------------------------------------")

            print("------------------------------------------------------------------")
            infallocated = True

        elif allocatechoice == "2":
            while True:
                print("Allocating budget for NPCC")
                print("---------------------------------")
                print("Date:")
                day = input("Enter day: ")
                month = input("Enter month: ")
                year = input("Enter year: ")
                time = input("Enter time (Military Time): ")
                if day.isdigit() and month.isdigit() and year.isdigit() and time.isdigit():
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    time = int(time)
                    if day > 0 and month > 0 and year > 0 and len(str(year)) == 4 and time > 0 and len(str(time)) == 4:
                        if day < 32 and month < 13:
                            if time < 2400:
                                break
                print("One or more inputs wrong, try again")
            while True:
                amountallocated = input("Enter amount to allocate: ")
                if amountallocated.isdigit() and int(amountallocated) > 0:
                    break
                print("Invalid input, try again")
            addexpense("NPC", day, month, year, time, amountallocated, "Allocation")
            print("NPCC budget allocated (" + str(amountallocated) + ")")
            print("------------------------------------------------------------------")
            print("------------------------------------------------------------------")
            npcallocated = True

        elif allocatechoice == "3":
            while True:
                print("Allocating budget for Floorball")
                print("---------------------------------")
                print("Date:")
                day = input("Enter day: ")
                month = input("Enter month: ")
                year = input("Enter year: ")
                time = input("Enter time: ")
                if day.isdigit() and month.isdigit() and year.isdigit() and time.isdigit():
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    time = int(time)
                    if day > 0 and month > 0 and year > 0 and len(str(year)) == 4 and time > 0 and len(str(time)) == 4:
                        if day < 32 and month < 13:
                            if time < 2400:
                                break
                print("One or more inputs wrong, try again")
            while True:
                amountallocated = input("Enter amount to allocate: ")
                if amountallocated.isdigit() and int(amountallocated) > 0:
                    break
                print("Invalid input, try again")
            addexpense("FLO", day, month, year, time, amountallocated, "Allocation")
            print("Floorball budget allocated (" + str(amountallocated) + ")")
            print("------------------------------------------------------------------")
            floallocated = True

        elif allocatechoice == "4":
            break

        else:
            print("Invalid input, try again")






















def viewbudget():
  global setbudget
  global selectedcca
  global selectedccaname
  global selectedccaid
  setbudget()
  global CCA_budgets
  print("---------------------------------")
  print("|  VIEWING BUDGETS FOR ALL CCA  |")
  print("---------------------------------")
  print("---------------------------------")
  print("|INFOCOMM |   NPCC   | FLOORBALL |")
  print(f"|  {CCA_budgets[0]}   |   {CCA_budgets[1]}   |   {CCA_budgets[2]}  |")
  print("---------------------------------")
  while True:
    print("1. Exit & return to main menu")
    choice = input("Enter choice(1): ")
    if choice == "1":
      print("---------------------------------")
      print("|       RETURNING TO MENU       |")
      print("---------------------------------")
      return
    else:
      print("------------------")
      print("| INVALID INPUT  |")
      print("------------------")



def set_chosen_cca(choice):
  global selectedcca
  global selectedccaname
  global selectedccaid
  global selectedcca3letters
  if choice == "1":
    print("CCA1 selected")
    selectedccaname = "INFOCOMM "
    selectedccaid = 1
    selectedcca3letters = "INF"
    return
  elif choice == "2":
    print("CCA2 selected")
    selectedccaname = "NPCC     "
    selectedccaid = 2
    selectedcca3letters = "NPC"
    return
  elif choice == "3":
    print("CCA3 selected")
    selectedccaname = "FLOORBALL"
    selectedccaid = 3
    selectedcca3letters = "FLO"
    return
  else:
    print("Invalid input, restarting CCA selection")
def viewexpense():
    print("---------------------------------")
    print("|       VIEWING EXPENSES        |")
    print("---------------------------------")
    while True:
        print("Select CCA\n"
              "1. Infocomm\n"
              "2. NPCC\n"
              "3. Floorball\n"
              "4. Quit & Return to menu")
        ccachoice = input("Enter choice(1-4): ")
        if ccachoice == "4":
          print("---------------------------------")
          print("|       RETURNING TO MENU        |")
          print("---------------------------------")
          return

        elif ccachoice == "1" or ccachoice == "2" or ccachoice == "3":
            set_chosen_cca(ccachoice)
            print("---------------------------------")
            print("| VIEWING EXPENSES FOR " + selectedccaname + " |")
            print("---------------------------------")
            print("Day   Month   Year    Time    Amount     Reason")
            print("________________________________________________________________________________")
            expensenotexist = True
            if ccachoice == "1":
                if len(CCA_expenses) >= 7:
                    for i in range(len(CCA_expenses)):
                        if CCA_expenses[i] == "INF":
                            if i + 6 < len(CCA_expenses):
                                day = CCA_expenses[i + 1]
                                month = CCA_expenses[i + 2]
                                year = CCA_expenses[i + 3]
                                time = CCA_expenses[i + 4]
                                amount = CCA_expenses[i + 5]
                                reason = CCA_expenses[i + 6]
                                expensenotexist = False
                                if int(amount) < 0:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
                                else:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")

            elif ccachoice == "2":
                if len(CCA_expenses) >= 7:
                    for i in range(len(CCA_expenses)):
                        if CCA_expenses[i] == "NPC":
                            if i + 6 < len(CCA_expenses):
                                day = CCA_expenses[i + 1]
                                month = CCA_expenses[i + 2]
                                year = CCA_expenses[i + 3]
                                time = CCA_expenses[i + 4]
                                amount = CCA_expenses[i + 5]
                                reason = CCA_expenses[i + 6]
                                expensenotexist = False
                                if int(amount) < 0:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
                                else:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")
            elif ccachoice == "3":
                if len(CCA_expenses) >= 7:
                    for i in range(len(CCA_expenses)):
                        if CCA_expenses[i] == "FLO":
                            if i + 6 < len(CCA_expenses):
                                day = CCA_expenses[i + 1]
                                month = CCA_expenses[i + 2]
                                year = CCA_expenses[i + 3]
                                time = CCA_expenses[i + 4]
                                amount = CCA_expenses[i + 5]
                                reason = CCA_expenses[i + 6]
                                amount = str(amount)
                                spacetoreason =  10 - len(str(amount))
                                spacetoreason = int(spacetoreason)
                                expensenotexist = False
                                if int(amount) < 0:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}   {amount:<9}   {reason:<20}")
                                else:
                                    print(f"{day:>0} {month:>6} {year:>9} {time:>7}    {amount:<9}  {reason:<20}")

            elif expensenotexist:
                print("No existing expenses for " + selectedccaname)
            print("________________________________________________________________________________")


        else:
          print("------------------")
          print("| INVALID INPUT  |")

while True:

  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("|  INFOCOMM  |    NPCC     |  FLOORBALL  |")
  print("Select Action\n"
  "1. View budgets\n"
  "2. View expenses\n"
  "3. Add expenses\n"
  "4. Delete expenses\n"
  "5. Amend expenses\n"
  "6. Search expenses\n"
  "7. Allocate budget\n"
  "8. Chatbot\n"
  "9. Quit\n")

  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  choice = input("Enter choice(1-9): ")
  if choice  in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    if choice == "1":
      viewbudget()
      spaced()
    elif choice == "2":
      viewexpense()
      spaced()
    elif choice == "3":
      addexpenses()
      spaced()
    elif choice == "4":
      deleteexpense()
      spaced()
    elif choice == "5":
      amendexpense()
      spaced()
    elif choice == "6":
      searchexpense()
      spaced()
    elif choice == "7":
      allocatebudget()
      spaced()
    elif choice == "8":
      chatbot()
      spaced()
    elif choice == "9":
      break



  else:
    print("-----------------")
    print("| INVALID INPUT  |")
    print("-----------------")

