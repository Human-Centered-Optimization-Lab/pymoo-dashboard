<template>
	<div class="w-96 p-8 shadow-[5px_5px_#c6c6c6] dark:shadow-[5px_5px_#383d3f] bg-white dark:bg-[#181a1b] my-8">
		<h2 class="text-center block text-2xl font-bold my-4">
			{{ title }}
		</h2>
		<slot />
	</div>
</template>

<script>
export default {
	name: 'Widget',
	props: {
		title: {
			type: String,
			required: true
		}
	}
}
</script>