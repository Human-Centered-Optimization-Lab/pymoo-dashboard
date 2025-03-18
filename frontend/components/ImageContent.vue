<template>
	<img
		v-if="imageData && imageData.length > 0"
		:id="'graph-image-' + slugify(title)"
		class="image-content"
		:src="'data:image/gif; base64,' + imageData[currentIndex]"
		:alt="title"
	>
	<button
		class="move-button"
		type="button"
		@click="move(-1)"
	>
		<!-- eslint-disable-next-line vue/no-parsing-error -->
		<<
	</button>
	<input
		id="slider"
		type="range"
		:min="0"
		:max="imageData.length - 1"
		step="1"
		:value="currentIndex"
		@input="updateIndex($event.target.value)"
	>
	<button
		class="move-button"
		type="button"
		@click="move(1)"
	>
		>>
	</button>
	<!-- GenerateGif -->
	<GenerateGif
		:image-data="imageData"
		:title="title"
		style="margin-top: 15px;"
	/>
	<!--
	<a
		:href="'data:image/gif; base64,' + imageData[currentIndex]"
		:download="'graph-image-' + slugify(title) + currentIndex + 1 + '.gif'"
	>
		<span class="sr-only">Download image</span>
		<svg
			class="download-svg"
			xmlns="http://www.w3.org/2000/svg"
			role="img"
			fill="none"
			viewBox="0 0 24 24"
			stroke-width="1.5"
			stroke="currentColor"
		>
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
			/>
		</svg>
	</a>
	--->
</template>
<script>
import GenerateGif from './GenerateGif.vue'; // Import the GenerateGif component

export default {
	name: 'ImageContent',
	components: {
    	GenerateGif, // Register the GenerateGif component
	},
	props: {
		imageData: {
			type: Array,
			required: true
		},
		title: {
			type: String,
			required: true
		},
	},
	data() {
		return {
			index: null
		}
	},
	computed: {
		currentIndex() {
			return this.index ?? this.imageData.length - 1
		}
	},
	methods: {
		move(direction) {
			if (direction === -1)
				this.updateIndex(0)
			else
				this.updateIndex(this.imageData.length -1)
		},
		slugify(str) {
			return str.toLowerCase().trim().replace(/[^\w\s-]|(?:^-+)|(?:-+$)/g, '').replace(/\s+/g, '-')
			// I believe these are equivalent but the above is less replace operations and is more clear what is being replaced. If we run into issues, revert back to this
			//return str.toLowerCase().trim().replace(/[^\w\s-]/g, '').replace(/[\s_-]+/g, '-').replace(/(?:^-+)|(?:-+$)/g, '')
		},
		updateIndex(value) {
			if (value >= this.imageData.length - 1)
				return this.index = null
			this.index = value
		}
	}
}
</script>