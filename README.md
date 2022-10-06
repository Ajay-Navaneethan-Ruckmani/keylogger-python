# Disclaimer
## "DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."

# keylogger-python

This is a simple keylogger which was coded in python. When the program runs it creates a log file in the desktop. You can change it by changing the loggin-directory

To make the program run in background without getting a popup of cmd, use pythonw

Using pythonw
Just change the file extension of your python script from .py to .pyw and that’s it! Now, just double click the newly named .pyw file and it will run in the background.

To kill,
in windows, use 
~tasklist
~taskkill /PID <pid> pythonw.exe /F
