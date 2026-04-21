from binary_expression_tree import BinaryExpressionTree

def test_expression(infix, postfix, expected):
    """Test a single postfix expression."""
    try:
        tree = BinaryExpressionTree()
        tree.build_from_postfix(postfix)
        
        result = tree.evaluate_tree()
        infix_str = tree.infix_traversal()
        postfix_str = tree.postfix_traversal()
        
        # Check if result matches expected
        passed = abs(result - expected) < 0.0001
        status = "✓ PASS" if passed else "✗ FAIL"
        
        print(f"Infix Expression:   {infix}")
        print(f"Postfix Expression: {postfix}")
        print(f"Infix Traversal:    {infix_str}")
        print(f"Postfix Traversal:  {postfix_str}")
        print(f"Evaluated Result:   {result}")
        print(f"Expected Result:    {expected}")
        print(f"{status}")
        print("-" * 60)
        
        return passed
    except Exception as e:
        print(f"Infix Expression:   {infix}")
        print(f"Postfix Expression: {postfix}")
        print(f"✗ FAIL - Error: {e}")
        print("-" * 60)
        return False

def main():
    test_cases = [
        ("(5 + 3)", "5 3 +", 8.0),
        ("((8 - 2) + 3)", "8 2 - 3 +", 9.0),
        ("(5 + (3 * 8))", "5 3 8 * +", 29.0),
        ("((6 / 2) + 3)", "6 2 / 3 +", 6.0),
        ("((5 + 8) - 3)", "5 8 + 3 -", 10.0),
        ("((5 + 3) * 8)", "5 3 + 8 *", 64.0),
        ("((8 + (2 * 3)) - 6)", "8 2 3 * + 6 -", 8.0),
        ("((5 + (3 * 8)) / 2)", "5 3 8 * + 2 /", 14.5),
        ("((8 + 2) - (3 * 6))", "8 2 + 3 6 * -", -8.0),
        ("((5 + 3) - (8 / 2))", "5 3 + 8 2 / -", 4.0),
    ]
    
    print("=" * 60)
    print("BINARY EXPRESSION TREE ADT TESTS")
    print("=" * 60)
    
    passed_count = 0
    for infix, postfix, expected in test_cases:
        if test_expression(infix, postfix, expected):
            passed_count += 1
    
    print(f"\nTotal: {passed_count}/{len(test_cases)} tests passed")

if __name__ == "__main__":
    main()
