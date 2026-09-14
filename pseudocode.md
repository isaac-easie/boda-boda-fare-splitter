BEGIN
    // Input n requirements 4 distance
    TRY
        INPUT distance_text
        CONVERT distance_text TO float distance
    CATCH ValueError
        PRINT "Invalid distance. Please enter a number."
        RETURN
    END TRY
    
    IF distance <= 0 THEN
        PRINT "Distance must be greater than zero."
        RETURN
    END IF
    
    // Input & Validation for Peak Hours
    INPUT peak_choice
    CONVERT peak_choice TO lowercase and stripped text
    
    IF peak_choice NOT IN ("1", "0", "peak", "off-peak", "off peak", "offpeak") THEN
        PRINT "Invalid travel hour choice. Please choose 1 or 0."
        RETURN
    END IF
    
    //Input Voucher Code
    INPUT voucher_code
    CONVERT voucher_code TO uppercase and stripped text
    
    //Set Fare Constants
    SET base_fee = 4000
    SET rate_per_km = 1200
    SET peak_rate = 0.10
    SET discount_amount = 1500
    SET number_of_students = 3
    
    //Core Calculations
    SET distance_cost = distance * rate_per_km
    
    IF peak_choice EQUALS "1" OR peak_choice EQUALS "peak" THEN
        SET peak_surcharge = distance_cost * peak_rate
    ELSE
        SET peak_surcharge = 0
    END IF
    
    SET gross_total = base_fee + distance_cost + peak_surcharge
    
    IF voucher_code EQUALS "UCU1500" THEN
        SET discount = discount_amount
    ELSE
        SET discount = 0
    END IF
    
    SET total_trip_cost = gross_total - discount
    SET student_share = ROUND(total_trip_cost / number_of_students, 2)
    
    // Output Results
    PRINT "trip summary"
    PRINT "Distance travelled: ", distance, " km"
    PRINT "Distance cost: UGX ", distance_cost
    PRINT "Base call out fee: UGX ", base_fee
    PRINT "Peak surcharge: UGX ", peak_surcharge
    PRINT "Discount: UGX ", discount
    PRINT "Total trip cost: UGX ", total_trip_cost
    PRINT "Number of students: ", number_of_students
    PRINT "Amount payable by each student: UGX ", student_share
    PRINT "Thank you for using the fare splitter!"
END MainProgram

BEGIN OuterLoop
    WHILE True DO
        CLEAR SCREEN
        CALL MainProgram
        
        INPUT user_input
        IF user_input EQUALS "exit" THEN
            PRINT "Exiting the program..."
            BREAK LOOP
        END IF
    END WHILE
END OuterLoop


//OKONYA ISAAC M26D14/007    MUDENYA AMOS M26D14/018    NAMUBIRU FAITH M26B13/036
