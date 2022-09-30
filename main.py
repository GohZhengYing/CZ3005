import task1
import task2
import task3

energy_budget = 287932

if __name__ == "__main__":
    main()

def main():
    user_choice = input("Choose which task number to run [1 or 2 or 3]: ")

    if user_choice == 1:
        continue
    elif user_choice == 2:
        task2.task2_search("1", "50", energy_budget)
    elif user_choice == 3:
        task3.run()
    else:
        print("Task not found! Exiting application!")
        exit()


