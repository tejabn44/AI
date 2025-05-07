def evaluate_performance():
    print("Employee Performance Evaluation Expert System\n")
    
    # Taking input for different performance criteria
    work_quality = input("Rate the work quality (poor/average/good): ").lower()
    work_consistency = input("Rate the work consistency (poor/average/good): ").lower()
    teamwork = input("Rate the teamwork (poor/average/good): ").lower()
    leadership = input("Rate the leadership (poor/average/good): ").lower()
    communication = input("Rate the communication (poor/average/good): ").lower()
    
    # Define evaluation rules
    performance_score = 0
    
    # Assigning score based on input
    criteria = [work_quality, work_consistency, teamwork, leadership, communication]
    for criterion in criteria:
        if criterion == 'good':
            performance_score += 2
        elif criterion == 'average':
            performance_score += 1
        elif criterion == 'poor':
            performance_score += 0
    
    # Evaluate overall performance based on the score
    if performance_score >= 8:
        performance_grade = "Excellent"
    elif 5 <= performance_score < 8:
        performance_grade = "Satisfactory"
    else:
        performance_grade = "Needs Improvement"
    
    print(f"\nEmployee's overall performance: {performance_grade}")
    
# Run the evaluation
evaluate_performance()
