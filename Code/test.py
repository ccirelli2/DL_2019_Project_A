



for col in list_col_names:

    print('Starting function for col {}'.format(col))

    # Get Text Associated With This Label
    label = col[:1]                                      # drops off the _ from the end

    # Retreive the Text Associated With This Label
    df_text = m3.get_text_4_specific_label(mydb, label)

    # Create a Dictionary for Count of Matched Tokens
    Dict_matched_tokens = {}

    for row_text in df_text.itertuples():
        clean_tokenize_text = m1.clean_and_tokenize_text(row_text[2])
        
        for token in list_tokens:
            if token in clean_tokenize_text:
                Dict_matched_tokens[token] = Dict_matched_tokens.get(token, 0) + 1

   # Update- Completion Dict 
   print('Dictionary completed for col {}'.format(col))

    # Insert Token Freq Into Database 
    for token in Dict_matched_tokens:
        token_freq =  round(((Dict_matched_tokens[token] / Num_tokens) * 100),4)

        # Insert
        m3.insert_token_freq(mydb, mycursor, col, token_freq, token)

    # Update - Completion of Col
    print('Insertion completed for col {}\n'.format(col))

