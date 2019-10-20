#/usr/bin/bash

function getFileListing()
{
	filelistQA=$(ls -lrt $1 | cut -d" " -f9)
	output=$(ls -lrt $1 | grep -v "$IgnorefilelistProduction" | cut -d" " -f9)
	for tempBuildNumber in $filelistQA
	do
		buildNumber=$(echo "$tempBuildNumber" | cut -d"." -f1 | cut -d"-" -f3)
		#echo "Build Number : $buildNumber  Min : $min Max: $max"
		if ((10#$buildNumber>=10#$min && 10#$buildNumber<=10#$max ));
		then
			buildname=$tempBuildNumber
			output=$(echo "$output" | grep -v $buildname )
		fi
	done
	echo $output
}


#Main Block
export location=$(dirname $0)
if [ "$location" == "." ]
then
      location=$(pwd)
fi
IgnorefilelistProduction=$(ls -lrt $location/application/dist/production | tail -3  | cut -d" " -f9)
min=$(ls -lrt $location/application/dist/production | tail -3  | cut -d" " -f9 | head -1 | cut -d"." -f1 | cut -d"-" -f3)
max=$(ls -lrt $location/application/dist/production | tail -3  | cut -d" " -f9 | tail -1 | cut -d"." -f1 | cut -d"-" -f3)
echo "IgnorefilelistProduction : $IgnorefilelistProduction"
echo "Range : $min and $max"
# To delete filelistQA, delete only when confirm with output
outputQA=$(getFileListing "application/dist/qa")
echo "OUTPUTQA : $outputQA"
cd "$location/application/dist/qa"
pwd
echo "rm -fr $outputQA"
#rm -fr $outputQA
cd $location
ls -lrt application/dist/qa

# To delete filelistIntegration, delete only when confirm with output
outputIntegration=$(getFileListing "application/dist/integration")
echo "outputIntegration : $outputIntegration" 
cd "$location/application/dist/integration"
pwd
echo "rm -fr $outputIntegration"
#rm -fr $outputIntegration
cd $location
ls -lrt application/dist/integration

