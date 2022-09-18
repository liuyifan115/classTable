<template>
	<view class="content">
		<view class="input"><input placeholder="请输入团队id" v-model="teamid"/></view>
		<view class="button"><button @click="jointeam">加入</button></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				teamid: '',
				username: uni.getStorageSync('username')
			}
		},
		methods: {
			jointeam() {
				let that=this
				uni.request({
						url: 'http://127.0.0.1:8000/lesson/jointeam',
						method: 'POST',
						data: {
							teamid: this.teamid,
							username: this.username,
						},
						
						
					success: (res) => {
						if (res.data.status_code == '-114514'){
							uni.showToast({
								icon:'error',
								title:'你已经在团队了',
							})}
						else if (res.data.status_code == '-114'){
							uni.showToast({
								icon:'error',
								title:'团队不存在',
							})
						}
						else
						{
						uni.setStorageSync('teamname', res.data.teamname)
						uni.showToast({
							title: 'ok',
							duration: 2000
						})
						uni.navigateTo({
							url: '../main/main'
						})
						}}
			
					})
				},
		}
	}
</script>

<style>
.content{
	display: flex;
	flex-direction: column;
}
	
.input{
	display: flex;
	align-self: center;
	justify-self: center;
	align-content: center;
	justify-content: center;
	margin: 20rpx;
	width: 500rpx;
	background-color: whitesmoke;
	padding: 15rpx;
	border-radius: 30rpx;
}

.button{
	align-self: center;
	margin: 20rpx;
	border-radius: 30rpx;
	height: 50rpx;
	width: 200rpx;
}
</style>
