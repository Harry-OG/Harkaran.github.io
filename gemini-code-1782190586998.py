def guard_bot(user_query):
    query = user_query.lower()
    
    if "scam" in query or "fraud" in query:
        return "⚠️ Tip: Never share OTPs, UPI PINs, or click on urgent-sounding links claiming your account is blocked!"
    elif "password" in query:
        return "🔐 Tip: Use a mix of uppercase, lowercase, numbers, and symbols. Switch to a Passkey or Password Manager if possible."
    elif "career" in query or "cybersecurity" in query:
        return "🚀 Career Info: Cybersecurity is booming! Look into roles like Ethical Hacker, Digital Forensics Analyst, or Security Architect."
    elif "help" in query:
        return "I can help you with: 1. Scam Prevention | 2. Password Safety | 3. Cybersecurity Careers. Type your keywords!"
    else:
        return "🤖 I'm still learning! For urgent help, report cyber crimes at your local cyber cell or official national portal."

# Example Usage
print(guard_bot("How do I protect against a scam?"))