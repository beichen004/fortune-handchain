
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const sign = urlParams.get('sign') || 'aries';
    const day = urlParams.get('day') || 'today';
    const apiUrl = 
`http://127.0.0.1:5000/api/fortune/daily/${sign}/${day}`;
    console.log('API URL:', apiUrl);
    fetch(apiUrl)
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) throw new Error(`HTTP error! Status: 
${response.status}`);
            return response.json();
        })
        .then(data => {
            console.log('Data:', data);
            if (data.success) {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('sign').textContent = `星座: 
${data.sign}`;
                document.getElementById('day').textContent = `日期: 
${data.day}`;
                document.getElementById('fortune').textContent = `运势: 
${data.fortune}`;
            } else {
                throw new Error('API 返回失败');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('loading').textContent = 
'加载失败，请稍后重试: ' + error.message;
        });
});

