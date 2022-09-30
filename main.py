import task1
import task2
import task3

energy_budget = 287932



def main():
    print("Task 1")
    task1.print_path("", task1.findminpath('1', '50', task1.g, task1.dist))
    print("\nTask 2\n")
    task2.task2_search("1", "50", energy_budget)
    print("\nTask 3\n")
    task3.run(9.6)


if __name__ == "__main__":
    main()
