Step 1: Install Streamlit
    pip install streamlit

Step 2:
    pip install -r requirements.txt

Step 3: Run the GUI App
    streamlit run SecurityPyApp.py

Incase command not found for streamlit then follow below step: 
    ✅ Step 1: Check if Streamlit is Installed
                pip show streamlit
                
                If you get output → it’s installed, just not available in your terminal’s PATH.

                If you get WARNING: Package(s) not found → it’s not installed.

                    ✅ Step 2: Install Streamlit (if needed)

                        Option A: Global install
                            pip install streamlit
                        Option B: Using python3
                            python3 -m pip install streamlit
                        Option C: You're using a virtual environment?
                            Then activate it:
                                source venv/bin/activate
                            Then install:
                                pip install streamlit
                    ✅ Step 3: Run Streamlit with Full Path (if still broken)
                        If streamlit still doesn’t work, try:
                                python3 -m streamlit run SecurityPyApp.py

🚀 Bonus: Add Streamlit to PATH (optional)
        export PATH=$HOME/.local/bin:$PATH
Then try again:
        streamlit run SecuPyApp.py


Note:
1.  Locally, this will launch at http://localhost:8501.
2.  On AWS EC2, open port 8501 in your Security Group, then go to http://<your-ec2-ip>:8501
   