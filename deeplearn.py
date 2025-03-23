import deepl

auth_key = "9ebf00e0-2bb1-4bd0-b187-7b9f2ac82c5c:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

inputText = """Sorting of filenames in android is confusing"""
result = translator.translate_text(inputText, target_lang="EN-US", context="This is a tech document, so the formal word which is widely used in git hub document if preferred")
print(result.text)  # "Bonjour, le monde !"