<template>
	<view class="content">
		<view>登录</view>
		<view>
			<input v-model="username" placeholder="用户名"/>
			<input v-model="userpassword" placeholder="密码" type="password"/>
			<button @click="submit">登录</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				username: '',
				userpassword: '',
				teamid:'',
			}
		},
		onLoad() {
				let that=this
				uni.request({
						url: 'http://127.0.0.1:8000/lesson/teamtable',
						method: 'POST',
						data: {
							teamid: uni.getStorageSync('teamid')
						},
						success: (res) => {
							uni.setStorageSync('teamTable', res.data.juti)
							}	
					})
		},
		methods: {
			submit() {
				let that=this
				uni.request({
						url: 'http://127.0.0.1:8000/lesson/gettable',
						method: 'POST',
						data: {
							'username': this.username,
							'userpassword': this.userpassword
						},
						
						
						success: (res) => {
							uni.setStorageSync('username', this.username)
							uni.setStorageSync('userpassword', this.userpassword)
							uni.setStorageSync('myTable', res.data.table)
							this.title = res.data.ans
							uni.switchTab({
								url: '../main/main'
							});
			
							}

			
			
			
			
					})
				},
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>
