import wk08


def main():
    pmf = {0: 0.8, 1: 0.15, 2: 0.04, 3: 0.01}

    p_1_2 = wk08.wk08(pmf, 1, 2)
    print(f"톱니바퀴에 1개 또는 2개의 결함이 발생할 확률 = {p_1_2}")

    p_1_3 = wk08.wk08(pmf, 1, 3)
    print(f"톱니바퀴에 1개 ~ 3개의 결함이 발생할 확률 = {p_1_3}")


if "__main__" == __name__:
    main()
