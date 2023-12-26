from human import Human, HumanGender


def main():
    ivan = Human("Иван", HumanGender.male)
    ivan.introduce()


if __name__ == "__main__":
    main()
