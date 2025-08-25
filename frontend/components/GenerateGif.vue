<template>
	<div>
		<button
			id="pause-button"
			@click="generateGif"
		>
			Download as GIF
		</button>
		<p v-if="!imageData || imageData.length === 0">
			No images available to generate GIF.
		</p>
	</div>
</template>
  
<script>
import gifshot from 'gifshot'
  
export default {
    props: {
      imageData: {
        type: Array,
        required: true
      },
      title: {
        type: String,
        required: true
      }
    },
    methods: {
        generateGif() {
            if (!this.imageData || this.imageData.length === 0) {
                console.error("No images to create GIF")
                return
            }
    
            const images = this.imageData.slice(0, this.imageData.length)
    
            gifshot.createGIF(
            {
                images: images.map(img => img.startsWith('data:image') ? img : `data:image/png;base64,${img}`),
                gifWidth: 500,
                gifHeight: 500,
                interval: 0.2 // Seconds per frame
            },
            (obj) => {
                if (!obj.error) {
                    const gifUrl = obj.image
        
                    // Create a download link
                    const a = document.createElement('a')
                    a.href = gifUrl
                    a.download = `${this.title}.gif`
                    document.body.appendChild(a)
                    a.click()
                    document.body.removeChild(a)
                } else {
                    console.error("GIF generation error:", obj.error)
                }
            })
        }
    }
}
</script>