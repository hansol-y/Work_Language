# Work_Language

## Application Introduction
**Work-Language** is a lightweight app application that transforms emotionally raw or unfiltered thoughts into work-appropriate communication. Designed for professionals, interns, or anyone navigating difficult workplace conversations, it enables users to express their intent clearly—while adjusting tone and formality through a simple interface.

### Key Features
- Raw Input Handling
    - Users can freely express what they really want to say in a multi-line text box.
    - Inputs are editable and can be cleared for quick reset.
- Tone Adjustment (Level 1–5)
    - A tone slider allows users to control how polite or direct the rewritten message should be.
    - Level 1 = very polite and indirect <br> Level 5 = direct but still workplace-acceptable
- Message Conversion
    - Send the input to the backend for transformation by pressing "Enter" or "Send" buttons
    - A loading indicator provides feedback during processing.
    - The button is temporarily disabled to prevent duplicate requests.
- Clear Output Display
    - The rewritten message is shown below the input area.
    - It is visually distinct from the original message and easily reviewable.
- Follow-Up Refinement
    - Users can ask for follow-up adjustments to further refine the rewritten message.
    - Follow-up prompts (e.g., “Make it sound more urgent” or “Soften this a bit”) use the original input as the anchor context.
    - This enables a natural, conversational refinement loop.

## DoD
- User can enter emotionally raw input (free-form) into a text box
    - The input box accepts multi-line text
    - Input must be editable and cleared/resettable
- User selects tone level (1-5) from a slider 
    - Tone 1 = very polite, Tone 5 = honest/direct
- User presses the "Send" button or "Enter" in their keyboard
    - Converstation starts with visible loading indicator
    - Button is disabled while conversion is in progress
- Output appears below input
    - Output text reflects the adjusted tone level
    - Output is clearly distinguishable from the original
- User can ask for the follow-ups for more customized refinement
    - The input box accepts multi-line text
    - Input must be editable and cleared/resettable
    - The conversation should refine the **initial input** based on the new request