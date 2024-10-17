<template>
	<dialog ref="dialog" class="group pointer-events-none open:pointer-events-auto opacity-0 invisible open:visible open:opacity-100 grid transition-[opacity,backdrop-filter,visibility] fixed inset-0 backdrop:[transition:backdrop-filter_.5s_ease] backdrop-blur-sm bg-black/20 h-full w-full z-40 max-h-none max-w-none">
		<div class="h-full overflow-y-auto">
			<div class="motion-safe:animate-closeModal motion-safe:group-open:animate-openModal my-20 z-50 bg-white dark:bg-[#181a1b] text-black dark:text-[#e8e6e3] w-full max-w-[95vw] sm:max-w-lg data-[help=true]:max-w-screen-md rounded-lg shadow [--tw-shadow:0.3px_0.5px_0.7px_#0000001a,1.5px_2.9px_3.7px_-0.4px_#0000001a,2.7px_5.4px_6.8px_-0.7px_#0000001a,4.5px_8.9px_11.2px_-1.1px_#0000001a,7.1px_14.3px_18px_-1.4px_#0000001a,11.2px_22.3px_28.1px_-1.8px_#0000001a,17px_33.9px_42.7px_-2.1px_#0000001a,25px_50px_62.9px_-2.5px_#0000001a] [--tw-shadow-colored:0.3px_0.5px_0.7px_var(--tw-shadow-color),1.5px_2.9px_3.7px_-0.4px_var(--tw-shadow-color),2.7px_5.4px_6.8px_-0.7px_var(--tw-shadow-color),4.5px_8.9px_11.2px_-1.1px_var(--tw-shadow-color),7.1px_14.3px_18px_-1.4px_var(--tw-shadow-color),11.2px_22.3px_28.1px_-1.8px_var(--tw-shadow-color),17px_33.9px_42.7px_-2.1px_var(--tw-shadow-color),25px_50px_62.9px_-2.5px_var(--tw-shadow-color)] relative m-auto p-8">
				<h2 class="text-center block text-2xl font-bold my-4">
					{{ title }}
				</h2>
				<img v-if="imageData && imageData.length > 0" @click="openModal"
					v-bind:src="'data:image/gif; base64,' + imageData[currentIndex]"
					:id="'graph-image-' + slugify(title)" :alt="title" class="w-full" />
				<input class="w-full" type="range" :min="0" :max="imageData.length - 1" step="1" v-bind:value="currentIndex"
					@input="updateIndex($event.target.value)" />
				<a v-bind:href="'data:image/gif; base64,' + imageData[currentIndex]" :download="'graph-image-' + slugify(title) + currentIndex + 1 + '.gif'">
					<span class="sr-only">Download image</span>
					<svg xmlns="http://www.w3.org/2000/svg" role="img" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-[1em] inline-block">
						<path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
					</svg>
				</a>
			</div>
		</div>
		<form class="fixed inset-0 text-transparent" method="dialog">
			<button class="h-full w-full cursor-default" type="submit">Close</button>
		</form>
	</dialog>
	<Widget :title="title" :id="'plot-wrapper-' + slugify(title)" @click="openModal" class="cursor-pointer peer-open:hidden [dialog[open]+&]:hidden">
		<img v-if="imageData && imageData.length > 0"
			v-bind:src="'data:image/gif; base64,' + imageData[currentIndex]"
			:id="'graph-image-' + slugify(title)" :alt="title" class="w-full" />
		<input ref="slider" class="w-full" type="range" :min="0" :max="imageData.length - 1" step="1" v-bind:value="currentIndex"
			@input="updateIndex($event.target.value)" />
		<a ref="download" v-bind:href="'data:image/gif; base64,' + imageData[currentIndex]" :download="'graph-image-' + slugify(title) + currentIndex + 1 + '.gif'">
			<span class="sr-only">Download image</span>
			<svg xmlns="http://www.w3.org/2000/svg" role="img" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-[1em] inline-block">
				<path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
			</svg>
		</a>
	</Widget>
</template>
<script>
import Widget from './Widget.vue'
export default {
	name: 'ImageWidget',
	props: {
		imageData: {
			type: Object,
			required: true
		},
		title: {
			type: String,
			required: true
		},
	},
	methods: {
		slugify(str) {
			return str.toLowerCase().trim().replace(/[^\w\s-]|(?:^-+)|(?:-+$)/g, '').replace(/\s+/g, '-')
			// I believe these are equivalent but the above is less replace operations and is more clear what is being replaced. If we run into issues, revert back to this
			//return str.toLowerCase().trim().replace(/[^\w\s-]/g, '').replace(/[\s_-]+/g, '-').replace(/(?:^-+)|(?:-+$)/g, '')
		},
		openModal(e) {
			console.log('is open', this.$refs.dialog.open)
			const whitelist = [this.$refs.slider, this.$refs.download]
			if (whitelist.includes(e.target) || whitelist.includes(e.currentTarget))
				return
			this.$refs.dialog.showModal()
		},
		updateIndex(value) {
			if (value >= this.imageData.length - 1)
				return this.index = null
			this.index = value
		}
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
	}
}
</script>