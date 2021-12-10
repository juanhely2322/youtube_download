 

function descargarVideo() {
      fetch('http://localhost:5000/calidad?enlace={{ enlace }}')
      .then(res => res.json())
      .then(response => {
                
                const link = document.createElement("a");
                link.download = 'video';
                link.href = response.url;
                link.click();
            })
    }

