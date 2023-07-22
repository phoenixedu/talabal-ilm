import os
def create_html_files(file_names):
    for file_name in file_names:
        # Create the file path
        file_path = f"{file_name}.html"
        
        # Create the HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{file_name}</title>
        </head>
        <body>
            <h1>{file_name}</h1>
            <p>This is the content of {file_name} file.</p>
        </body>
        </html>
        """
        
        # Write the content to the file
        with open(file_path, "w") as file:
            file.write(html_content)
        
        print(f"Created {file_path}")

# List of file names to create
file_names = ['classForm','listOfClasses','classD','addstudentList','createLeture']

# Call the function to create the HTML files
create_html_files(file_names)


