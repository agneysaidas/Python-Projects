# 🔐 Caesar Cipher Encoder / Decoder 🔄

Welcome to the Caesar Cipher Python project! </br>
This fun little tool allows you to encrypt 🔒 and decrypt 🔓 messages using the classic Caesar Cipher — one of the oldest encryption techniques in history.

## 🧠 What is a Caesar Cipher?

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is "shifted" a certain number of places down or up the alphabet.

<pre> > For example, with a shift of <code>3</code>: ></br> <code>a</code> ➡️ <code>d</code>, <code>b</code> ➡️ <code>e</code>, <code>z</code> ➡️ <code>c</code> </pre>

It wraps around the alphabet, so it’s perfect for basic encryption tasks and learning about cryptography!

## 💻 Features

✅ Encode and decode messages
✅ Handles spaces, punctuation, and symbols
✅ Wrap-around support (i.e., z becomes c)
✅ Option to run again or exit
✅ Fun ASCII art logo via the art package 🎨

##▶️ How to Use
1. Make sure both caesar_cipher.py and art.py are in the same folder.
2. Run the script with:
```bash
python caesar_cipher.py
```

## 📝 Sample Interaction

```python
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi!
Type 'yes' if you want to go again. Otherwise, type 'no'.
> no
Good Bye!
```

## 📁 File Structure

```bash
📦 caesar-cipher/
 ┣ 📜 caesar_cipher.py
 ┣ 📜 art.py
 ┗ 📄 README.md
```

## 👨‍💻 Author
Made with ❤️ by Agney 📫 Feel free to connect or contribute!
