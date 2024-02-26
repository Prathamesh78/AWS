# Instructions for Creating Public S3 Bucket and Uploading an Object

This guide provides step-by-step instructions to create an Amazon S3 bucket, enable public access, upload an object to it, and generate a public URL.

### Steps:
1. **Create S3 Bucket:**
```bash
aws s3api create-bucket --bucket your-bucket-name --region your-region --create-bucket-configuration LocationConstraint=your-region
```

2. **Enable Public Access:**
- Create a bucket policy allowing public read access.
- Create a policy.json
```bash
{
  "Id": "Policy1708927166978",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1708925649664",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::demo-prathamesh78/*",
      "Principal": "*"
    }
  ]
}
```
- Apply the policy to the bucket.
```bash
aws s3api put-bucket-policy --bucket your-bucket-name --policy file://policy.json
```

3. **Upload an Object:**
```bash
aws s3 cp path/to/your/object s3://your-bucket-name/
```

4. **Generate Public URL:**
```bash
aws s3 presign s3://your-bucket-name/your-object-name --expires-in 604800
```
