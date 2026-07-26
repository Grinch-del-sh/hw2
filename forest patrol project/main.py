def main():
    print("===== FOREST PATROL (console game) =====")
    try:
        rows = int(input("Enter number of rows (10-30): ") or "15")
        cols = int(input("Enter number of columns (10-40): ") or "20")
        rows = max(10, min(30, rows))
        cols = max(10, min(40, cols))
    except:
        rows, cols = 15, 20

    game = Game(rows, cols)
    game.run()

if __name__ == "__main__":
    main()