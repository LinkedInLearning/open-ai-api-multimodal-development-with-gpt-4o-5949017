import json
from utils.openai_init import openai_init
from utils.encode_image import encode_image
from utils.manage_data import add_rows
from utils.function_call import function_call

client = openai_init()

def process_receipt(expenses_df, image_path):
    """
    Process a receipt image using a completion model.

    Parameters:
    client: The client object to interact with the completion model.
    image_path (str): The path to the receipt image file to be processed.

    Returns:
    dict: The processed receipt data.
    """
    
    # Encode the image
    print(f"Encoding image: {image_path}")
    base64_image = encode_image(image_path)

    # Create the completion request
    print(f"Passing image data to GPT-4o for processing...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a processor of receipts. If the provided image is not a receipt, DON'T DESCRIBE IT! Ask for a receipt."},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                }
            ]},
        ],
        tools=function_call,
        tool_choice="auto",
        temperature=0.0,
    )

    if response:
        print(f"Response received from GPT-4o: {response}")

        # If the image is a receipt, process the data
        if (response.choices[0].message.tool_calls is not None and 
            len(response.choices[0].message.tool_calls) > 0 and 
            response.choices[0].message.tool_calls[0].function.name == "itemize_receipt"):
    
            # Extract receipt data from the response
            receipt_data = json.loads(response.choices[0].message.tool_calls[0].function.arguments)

            # print(receipt_data)
            print(f"\nRetrieved receipt data from {receipt_data['date']} at {receipt_data['vendor']}")

            # Add the receipt data to the expenses DataFrame
            expenses_df = add_rows(expenses_df, receipt_data)
        
        else:
            print(f"\nWARNING:\n{response.choices[0].message.content}")
            
    else:
        print("No response received from GPT-4o.")
    
    return expenses_df

    
