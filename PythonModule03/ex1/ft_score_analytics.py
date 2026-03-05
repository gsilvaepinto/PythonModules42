import sys

if __name__ == '__main__':
    print("=== Player Score Analytics ===")
    score = sys.argv[1:]
    if len(score) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        sys.exit(1)
    try:
        converted = [int(arg) for arg in score]
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"Scores processed: {converted}")
    print(f"Total players: {len(converted)}")
    print(f"Total score: {sum(converted)}")
    print(f"Average score: {sum(converted) / len(converted)}")
    print(f"High score: {max(converted)}")
    print(f"Low score: {min(converted)}")
    print(f"Score range: {max(converted) - min(converted)}")
