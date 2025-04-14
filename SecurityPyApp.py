import streamlit as st
from password_checker.check_password import check_strength, check_breach
from file_integrity.hash_checker import generate_hash
from network_scanner.scanner import scan_ports
from vulnerability_scanner.web_scanner import scan_sql_injection

# Page Setup
st.set_page_config(page_title="SecurityPyToolkit", layout="wide")
st.title("🛡️ SecurityPyToolkit - Combine basic Toolkit.")

tab1, tab2, tab3, tab4 = st.tabs(["🔐 Password Checker", "🧾 File Integrity", "🌐 Network Scanner", "🔍 Vulnerability Scanner"])

# ==================== Tab 1: Password Checker ====================
with tab1:
    st.header("🔐 Password Strength & Breach Checker")
    password = st.text_input("Enter Password", type="password")

    if st.button("Check Password"):
        strength = check_strength(password)
        breached = check_breach(password)
        st.write(f"**Strength Score:** {strength}/5")
        st.write("**Status:**", "⚠️ Breached" if breached else "✅ Safe")

# ==================== Tab 2: File Integrity ====================
with tab2:
    st.header("🧾 File Integrity Checker")
    uploaded_file = st.file_uploader("Choose a file to generate SHA256 hash")

    if uploaded_file:
        with open("temp_file", "wb") as f:
            f.write(uploaded_file.read())
        sha256 = generate_hash("temp_file")
        st.code(sha256, language="text")

# ==================== Tab 3: Network Scanner ====================
with tab3:
    st.header("🌐 Network Scanner")
    ip_address = st.text_input("Enter IP to scan")
    if st.button("Scan Ports"):
        if ip_address:
            open_ports = scan_ports(ip_address)
            st.success(f"Open Ports on {ip_address}:")
            for port in open_ports:
                st.write(f"🔓 Port {port} is open")

# ==================== Tab 4: Web Vulnerability Scanner ====================
with tab4:
    st.header("🔍 Basic Web Vulnerability Scanner")
    url = st.text_input("Enter URL to scan for SQLi (e.g. http://example.com/page?input=)")
    if st.button("Run SQLi Scan"):
        if url:
            results = scan_sql_injection(url)
            if results:
                for r in results:
                    st.warning(f"⚠️ Potential SQLi vulnerability at: {r}")
            else:
                st.success("✅ No obvious vulnerabilities detected.")
