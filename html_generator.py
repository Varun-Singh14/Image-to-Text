def generate_html(texts, visual_elements, output_html_path):
    html_content = "<html><body>"

    for text in texts:
        html_content += f"<p>{text}</p>"

    for element in visual_elements:
        html_content += f'<img src="{element}" alt="Visual Element">'

    html_content += "</body></html>"

    with open(output_html_path, "w") as html_file:
        html_file.write(html_content)
