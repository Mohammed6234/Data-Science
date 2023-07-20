import argparse

def calculate_average(physics, chemistry, maths):
    total_marks = physics + chemistry + maths
    average_marks = total_marks / 3
    return average_marks

def main():
    parser = argparse.ArgumentParser(description='Calculate average marks for three subjects.')
    parser.add_argument('--physics', type=int, required=True, help='Marks obtained in Physics')
    parser.add_argument('--chemistry', type=int, required=True, help='Marks obtained in Chemistry')
    parser.add_argument('--maths', type=int, required=True, help='Marks obtained in Maths')
    args = parser.parse_args()

    physics_marks = args.physics
    chemistry_marks = args.chemistry
    maths_marks = args.maths

    average_marks = calculate_average(physics_marks, chemistry_marks, maths_marks)
    print(f"Average marks for the three subjects: {average_marks:.2f}")

if __name__ == '__main__':
    main()


# python3 cmd.py --physics 60 --chemistry 70 --maths 90
