import streamlit as st

# Title of the app
st.title("Choosing the Right Statistical Test")

# Introduction
st.header("Introduction")
st.write("""
Choosing the appropriate statistical test depends on the nature of your data and the hypothesis you want to test. 
The following guide will help you understand when to use each statistical test and how to calculate it.
""")

# Creating Tabs for Different Tests
tabs = st.tabs(["When to Use t-Tests", "When to Use ANOVA", "When to Use Chi-Square"])

# Tab 1: t-Tests
with tabs[0]:
    st.header("When to Use t-Tests")
    st.write("""
    **One-Sample t-Test:**
    - Used when comparing the mean of a single sample to a known value (such as a population mean).
    - Example: Testing if the average height of a group of people is different from the known population mean height.

    **Paired Sample t-Test:**
    - Used when comparing the means of the same group at two different times or under two conditions (paired data).
    - Example: Comparing the performance of students before and after a training session.

    **Independent Two-Sample t-Test:**
    - Used when comparing the means of two independent groups.
    - Example: Comparing the exam scores of students from two different schools.
    """)

    # Code for t-Tests
    st.subheader("Example Code for t-Tests")
    code = '''
    import numpy as np
    from scipy import stats
    
    # One-Sample t-Test
    sample_data = [175, 160, 170, 180, 165, 155, 170, 175, 160, 165]
    population_mean = 170
    t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)
    print(f"One-Sample t-Test: t-Statistic = {t_statistic:.4f}, p-Value = {p_value:.4f}")
    
    # Paired Sample t-Test
    before = [23, 21, 18, 25, 30]
    after = [25, 23, 20, 27, 32]
    t_statistic, p_value = stats.ttest_rel(before, after)
    print(f"Paired Sample t-Test: t-Statistic = {t_statistic:.4f}, p-Value = {p_value:.4f}")
    
    # Independent Two-Sample t-Test
    group1 = [24, 28, 30, 25, 27]
    group2 = [22, 20, 23, 24, 21]
    t_statistic, p_value = stats.ttest_ind(group1, group2)
    print(f"Independent Two-Sample t-Test: t-Statistic = {t_statistic:.4f}, p-Value = {p_value:.4f}")
    '''
    st.code(code, language="python")

# Tab 2: ANOVA
with tabs[1]:
    st.header("When to Use ANOVA")
    st.write("""
    **One-Way ANOVA:**
    - Used when comparing the means of three or more independent groups.
    - Example: Testing if there is a difference in exam scores among students from three different schools.

    **Two-Way ANOVA:**
    - Used when studying the effect of two independent variables on a dependent variable.
    - Example: Examining the effect of two teaching methods (factor 1) and different age groups (factor 2) on student performance.
    """)

    # Code for ANOVA
    st.subheader("Example Code for One-Way ANOVA")
    code_anova = '''
    import numpy as np
    from scipy import stats
    
    # Sample data from 3 groups
    group1 = [24, 28, 30, 25, 27]
    group2 = [22, 20, 23, 24, 21]
    group3 = [32, 30, 35, 28, 31]
    
    # One-Way ANOVA
    f_statistic, p_value = stats.f_oneway(group1, group2, group3)
    print(f"One-Way ANOVA: F-Statistic = {f_statistic:.4f}, p-Value = {p_value:.4f}")
    '''
    st.code(code_anova, language="python")

# Tab 3: Chi-Square
with tabs[2]:
    st.header("When to Use Chi-Square Test")
    st.write("""
    **Chi-Square Test of Independence:**
    - Used when testing the association between two categorical variables.
    - Example: Testing if gender is associated with preference for a product.
    """)

    # Code for Chi-Square Test
    st.subheader("Example Code for Chi-Square Test")
    code_chi_square = '''
    import numpy as np
    from scipy import stats
    
    # Contingency table (observed frequencies)
    observed = np.array([[20, 30], [15, 25]])
    
    # Chi-Square test of independence
    chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)
    print(f"Chi-Square Test: Chi2-Statistic = {chi2_stat:.4f}, p-Value = {p_value:.4f}")
    '''
    st.code(code_chi_square, language="python")
